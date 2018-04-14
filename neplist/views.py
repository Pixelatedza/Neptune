from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core.files.base import ContentFile
from nepcore.views import NEPPaginatedView
from neplist.models import CheckList, Check
from neplist.forms import CheckForm
import datetime
import json
import base64
import os


class IndexView(TemplateView):
	template_name = "list/index.html"
	model = CheckList

class WorklistsView(NEPPaginatedView):
	model = CheckList
	queryset = CheckList.objects.all()

class CheckListView(TemplateView):
	template_name = "list/checklist.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["checklist"] = CheckList.objects.get(pk=self.kwargs.get('checklist_pk'))

		forms = []
		for check in context["checklist"].check_set.all():
			form = CheckForm(initial={'proof_file': check.proof_file, "checkPk": check.pk, "status": check.status})
			forms.append((check, form))
		context["forms"] = forms
		return context

class CheckView(TemplateView):

	def post(self, request):
		data = json.loads(self.request.body)
		check = Check.objects.get(pk=data["checkPk"])

		## Save Check
		if check:
			check.status = data["status"]
			if check.proof_file != data["proof_file"]:
				if os.path.isfile(check.proof_file.path):
					os.remove(check.proof_file.path)
					## Decode Base64 file
				format, imgstr = data["proof_file"].split(';base64,')
				ext = format.split('/')[-1]
				in_file = ContentFile(base64.b64decode(imgstr), name=str(datetime.datetime.now()) + "." + ext)
			
				check.proof_file = in_file

			check.save()
			return JsonResponse({'msg':'Success'}, status=200)

		errors = {"proof_file": "Something Went Wrong!"}
		return JsonResponse(errors, status=400)
