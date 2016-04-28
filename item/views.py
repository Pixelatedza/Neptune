from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import JsonResponse
import json
from item.forms import ItemTypeForm, ItemForm
from item.apps import HandleItemTypes
from django import forms as djForms
from nepcore.forms.fields import CUSTOM_FIELD_MAP

class CreateItemTypeView(TemplateView):
	"""View to create Item Types"""
	# TODO: I would like for the attribute form (dynamic form) to also work
	# from django forms. Formsets are the django way, but thanks to angular
	# this won't be necessary, a standard form with the correct ng-model binds
	# inside a ng-repeat will work perfectly.

	template_name = "item/create_item_type.html"

	def get(self, request):
		context = {"itemTypeForm":ItemTypeForm()}
		context['url'] = "/nepcore/item/create/item-type/"
		return self.render_to_response(context)

	def post(self, request):
		data = json.loads(self.request.body)
		handleItemTypes = HandleItemTypes(data)
		if handleItemTypes.is_valid():
			return JsonResponse({'msg':'Succesfully created Item Type'}, status=200)
		errors = handleItemTypes.errors
		return JsonResponse(errors, status=400)

class CreateItemView(TemplateView):
	"""View to create Items"""

	template_name = "item/dev.html"

	def get(self, request):
		form = ItemForm()
		form.fields['attr3'] = CUSTOM_FIELD_MAP['int'](label="Attr3")
		print dir(form)
		print form.fields
		context = {"itemForm":form}
		context['url'] = "/nepcore/item/create/"
		return self.render_to_response(context)

	def post(self, request):
		data = json.loads(self.request.body)
		handleItem = HandleItems(data)
		if handleItemTypes.is_valid():
			return JsonResponse({'msg':'Succesfully created Item'}, status=200)
		errors = handleItemTypes.errors
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