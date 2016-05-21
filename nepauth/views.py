from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from nepcore.views import NEPPaginatedView
import json

class AuthView(TemplateView):
	template_name = "auth/index.html"

class PagedUserView(NEPPaginatedView):
	model = User
	fields = ('username','email')