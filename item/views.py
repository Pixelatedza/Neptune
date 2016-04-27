from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import JsonResponse
import json
from item.forms import ItemTypeForm, ItemTypeAttributesForm
from item.apps import HandleItemTypes

class ItemTypeView(TemplateView):
	"""View to create Item Types"""

	template_name = "item/dev.html"

	def get(self, request):
		context = {"itemTypeForm":ItemTypeForm()}
		context['url'] = "/nepcore/item/"
		return self.render_to_response(context)

	def post(self, request):
		data = json.loads(self.request.body)
		hIT = HandleItemTypes(data)
		if hIT.is_valid():
			return JsonResponse({'msg':'Succesfully created Item Type'}, status=200)
		errors = hIT.errors
		print errors
		return JsonResponse(errors, status=400)

# HandleItems.create_type_with_attrs(d)
class ItemView(FormView):
	template_name = "item/dev.html"
	form_class = ItemTypeForm
	success_url = '/nepcore/item/'

	def form_valid(self, form):
		#print form.data
		d = {}
		d['itemType'] = form.data['itemType']
		d['attributes'] = []
		attributes = form.data['attributes'].split(',')
		for p in attributes:
			li = p.split('-')
			d['attributes'].append({'label':li[0],'_type':li[1]})
		#d['attributes'] = form.data['attributes'].split(',')
		#tempf(d)
		return super(IndexView, self).form_valid(form)