from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from nepcore.menu import menu
from nepcore.state import state_manager
import json

class BaseView(TemplateView):
	template_name = "nepcore/base_content.html"

	def get_context_data(self, **kwargs):
		context = super(BaseView, self).get_context_data(**kwargs)
		menu.auto_discover(self.request)
		context['menu'] = menu
		context['state_manager'] = state_manager
		return context

class IndexView(TemplateView):
	template_name = "nepcore/index.html"

class NEPPaginatedView(ListView):
	paginate_by = 2

	def get_context_data(self, **kwargs):
		context = super(NEPPaginatedView, self).get_context_data(**kwargs)
		context['paginateBy'] = self.paginate_by
		return context		

	def get(self, request, *args, **kwargs):
		self.kwargs['page'] = 1
		return super(NEPPaginatedView, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		self.json = json.loads(self.request.body)
		self.paginate_by = self.json.get('paginateBy', self.paginate_by)
		self.kwargs['page'] = self.json.get('page', 1)
		context = self.get_context_data()
		serialized_obj = serializers.serialize(
			'json',
			context[self.get_context_object_name(self.object_list)],
			fields=('username','email')
		)
		return JsonResponse(serialized_obj, status=200, safe=False)


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
