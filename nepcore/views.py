from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from nepcore.menu import menu
from nepcore.state import state_manager
from nepcore.models import NEPSiteConfig, NEPMenu
from django.conf import settings
import json

class BaseView(LoginRequiredMixin, TemplateView):
	template_name = "nepcore/base_content.html"

	def get_context_data(self, **kwargs):
		context = super(BaseView, self).get_context_data(**kwargs)
		menu.build_menu(self.request)
		context['menu'] = menu
		context['state_manager'] = state_manager
		return context

class IndexView(TemplateView):
	template_name = "nepcore/index.html"

class GetMenus(TemplateView):
	template_name = "nepcore/menus/menu.html"
	
	def get_context_data(self, **kwargs):
		context = super(GetMenus, self).get_context_data(**kwargs)
		menu.build_menu(self.request)
		context['menu'] = menu
		return context

class GetStates(TemplateView):

	def get(self, request, *args, **kwargs):
		states = state_manager.states_to_json()
		json = {"default_state": NEPSiteConfig.get_solo().default_view, "states":states}
		return JsonResponse(json, status=200, safe=False)

class NEPPaginatedView(ListView):
	paginate_by = 25
	fields = None

	def get_context_data(self, **kwargs):
		context = super(NEPPaginatedView, self).get_context_data(**kwargs)
		context['paginateBy'] = self.paginate_by
		return context

	def _serialize_paginator(self, paginator):
		return {
			'count': paginator.count,
			'perPage': paginator.per_page,
			'numPages': paginator.num_pages
		}

	def _serialize_page_obj(self, page_obj):
		json_obj = {
			'number': page_obj.number,
			'hasPrev': page_obj.has_previous(),
			'hasNext': page_obj.has_next(),
			'start': page_obj.start_index(),
			'end': page_obj.end_index()
		}
		if json_obj['hasPrev']:
			json_obj['prev'] = page_obj.previous_page_number()

		if json_obj['hasNext']:
			json_obj['next'] = page_obj.next_page_number()
		return json_obj

	def get(self, request, *args, **kwargs):
		self.kwargs['page'] = 1
		return super(NEPPaginatedView, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		self.json = json.loads(self.request.body)
		self.object_list = self.get_queryset()
		if len(self.json['filters']) > 0:
			filters = {}
			for f in self.json['filters']:
				if 'value' in f:
					filters['{0}'.format(f['field'])] = f['value']
			self.object_list = self.object_list.filter(**filters)

		allow_empty = self.get_allow_empty()
		
		if self.json.get('paginateBy'):
			self.paginate_by = self.json.get('paginateBy')

		self.kwargs['page'] = self.json.get('page', 1)
		context = self.get_context_data()
		context['paginator'] = self._serialize_paginator(context['paginator'])
		context['page_obj'] = self._serialize_page_obj(context['page_obj'])
		context['object_list'] = eval(serializers.serialize(
			'json',
			context['object_list'],
			fields=self.fields,
			use_natural_foreign_keys=True
		))
		context[self.get_context_object_name(self.object_list)] = eval(serializers.serialize(
			'json',
			context[self.get_context_object_name(self.object_list)],
			fields=self.fields,
			use_natural_foreign_keys=True
		))
		del context['view']
		return JsonResponse(context, status=200, safe=False)


class LoginView(TemplateView):
	template_name = 'nepcore/auth/login.html'

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		self.request.session.set_expiry(300)		
		context['next'] = self.request.GET.get('next',None)
		return context

	def get(self, request):
		context = self.get_context_data()
		logout(self.request)
		return self.render_to_response(context)

	def post(self, request):
		logout(self.request)
		data = json.loads(self.request.body)
		username = data['username']
		password = data['password']
		_next = data.get('next',None)

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(self.request, user)
				if _next:
					return JsonResponse({'msg':_next})
				else:
					return JsonResponse({'msg':'/nepcore/'})
			else: 
				return JsonResponse({'msg':'User not active'})
		else:
			return JsonResponse({'msg':'Invalid Username or Password'}, status=400)

class LogoutView(TemplateView):
	template_name = 'nepcore/auth/logout.html'

	def get_context_data(self, **kwargs):
		context = super(LogoutView, self).get_context_data(**kwargs)
		context['link'] = "/nepcore/login/"
		return context

	def get(self, request):
		context = self.get_context_data()
		logout(request)		
		return self.render_to_response(context)
