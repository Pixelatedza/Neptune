from django.views.generic import TemplateView
from nepcore.menu import menu
from nepcore.state import state_manager
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.views.generic.edit import FormView
from django.http import JsonResponse

class BaseView(TemplateView):
	template_name = "nepcore/base_content.html"

	def get_context_data(self, **kwargs):
		context = super(BaseView, self).get_context_data(**kwargs)
		context['menu'] = menu
		context['state_manager'] = state_manager
		return context

class IndexView(TemplateView):
	template_name = "nepcore/index.html"

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
