from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from nepcore.views import NEPPaginatedView
import json

class AuthView(TemplateView):
	template_name = "auth/index.html"

class GetGroupsView(TemplateView):

	def serialize_groups(self, groups):
		g = []
		for group in groups:
			g.append({
				"groupName": group.name,
				"groupPK": group.pk
			})
		return g

	def get(self, request, **kwargs):
		groups = self.serialize_groups(Group.objects.all())
		return JsonResponse(groups, status=200, safe=False)

class PagedUserView(NEPPaginatedView):
	model = User
	fields = ('username','email', 'groups')
	queryset = User.objects.exclude(pk=1)

class ChangeUserGroupView(TemplateView):
	
	def post(self, request):
		data = json.loads(self.request.body)
		try:
			user = User.objects.get(pk=data['user'])
			user.groups.clear()
			user.groups.add(data['group'])
			return JsonResponse({'msg': 'Group change successful'}, status=200)
		except:
			return JsonResponse({'msg': 'Something went wrong'}, status=400)
