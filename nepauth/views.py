from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from django.http import JsonResponse
import json

class AuthView(TemplateView):
	template_name = "auth/index.html"

	def get_context_data(self, **kwargs):
		context = super(AuthView, self).get_context_data(**kwargs)
		return context
