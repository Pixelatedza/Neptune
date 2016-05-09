from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import JsonResponse
import json
from item.forms import ItemTypeForm, ItemForm
from item.apps import HandleItemTypes, HandleItems
from django import forms as djForms
from nepcore.forms.fields import CUSTOM_FIELD_MAP

class ItemView(TemplateView):
	template_name = "item/items.html"

	def get_context_data(self, **kwargs):
		context = super(ItemView, self).get_context_data(**kwargs)
		context["itemTypes"] = HandleItemTypes.get_all_item_types()
		context["items"] = HandleItems.get_all_items()
		return context

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
		context["itemTypes"] = HandleItemTypes.get_all_item_types()
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

	template_name = "item/create_item.html"

	def get(self, request, itemName=None):
		form = ItemForm(initial={'itemType': itemName})
		fields = HandleItemTypes.get_item_type_attrs(itemName)
		for field in fields:
			form.fields[str(field['fieldId'])] = CUSTOM_FIELD_MAP[field['dataType']](label=field['label'])
		context = {"itemForm":form}
		context["itemName"] = itemName
		context['url'] = "/nepcore/item/create/"
		return self.render_to_response(context)

	def post(self, request):
		data = json.loads(self.request.body)
		handleItem = HandleItems(data)
		if handleItem.is_valid():
			return JsonResponse({'msg':'Succesfully created Item'}, status=200)
		errors = handleItem.errors
		return JsonResponse(errors, status=400)