from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django import template
from django import forms as djForms
from item.forms import ItemTypeForm, ItemForm
from item.apps import HandleItemTypes, HandleItems
from item.models import Item
from nepcore.forms.fields import CUSTOM_FIELD_MAP
from nepcore.views import NEPPaginatedView
import json

class ItemView(TemplateView):
	template_name = "item/items.html"

	def get_context_data(self, **kwargs):
		context = super(ItemView, self).get_context_data(**kwargs)
		context["itemTypes"] = HandleItemTypes.get_all_item_types()
		return context

class PagedItemView(NEPPaginatedView):
	paginate_by = 25
	model = Item
	fields = ('name','itemType')

class ItemTypeFields(TemplateView):

	def post(self, request):
		data = json.loads(self.request.body)
		fields_in = HandleItemTypes.get_item_type_attrs(data['itemName'])
		fields_out = []
		for field in fields_in:
			fields_out.append({
				'required': field.attribute.required,
				'default': field.attribute.defaultValue,
				'dataType': field.attribute.dataType,
				'label': field.attribute.label
			})
		return JsonResponse(fields_out, status=200, safe=False)

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

class CreateEditItemView(TemplateView):
	"""View to create Items"""

	template_name = "item/create_item.html"

	def get(self, request, itemTypePK=None, item=None):
		itemName = None
		itemValues = {'fields':{}}
		if item:
			itemValues = HandleItems.get_item_values(item)
			itemName = itemValues['item']
		form = ItemForm(initial={'itemType': itemTypePK, 'itemName': itemName, 'itemPK': item})
		fields = HandleItemTypes.get_item_type_attrs(itemTypePK)
		for field in fields:
			if field.attribute.label in itemValues['fields']:
				form.fields[str(field.attribute.id)] = CUSTOM_FIELD_MAP[field.attribute.dataType](
					label=field.attribute.label,
					initial=itemValues['fields'][field.attribute.label]
				)
			else:
				form.fields[str(field.attribute.id)] = CUSTOM_FIELD_MAP[field.attribute.dataType](
					label=field.attribute.label,
					initial=field.attribute.defaultValue
				)

		context = {"itemForm":form}
		context["itemTypePK"] = itemTypePK
		context['url'] = "/nepcore/item/create/"
		return self.render_to_response(context)

	def post(self, request):
		data = json.loads(self.request.body)
		handleItem = HandleItems(data)
		if handleItem.is_valid():
			return JsonResponse({'msg':'Succesfully created Item'}, status=200)
		errors = handleItem.errors
		return JsonResponse(errors, status=400)

class DeleteItemView(TemplateView):
	"""View to delete Items"""

	def post(self, request):
		data = json.loads(self.request.body)
		try:
			HandleItems.delete_item(data['itemPK'])
			return JsonResponse({'msg':'Succesfully created Item Type'}, status=200)
		except Exception as e:
			print e
			return JsonResponse({'msg':'Something went wrong'}, status=400)

class ExportItemView(TemplateView):

	def post(self, request):
		items = []
		data = json.loads(self.request.body)

		# Get all item information
		for itemPK in data:
			item = HandleItems.get_item_values(itemPK)
			items.append(item)

		# Generate CSV file
		tmpl = get_template('item/item_csv.csv')
		context = template.Context({'items': items})
		csv = tmpl.render(context)
		return HttpResponse(csv, status=200)

class EmailItemView(TemplateView):

	def post(self, request):
		items = []
		data = json.loads(self.request.body)

		# Get all item information
		for itemPK in data['items']:
			item = HandleItems.get_item_values(itemPK)
			items.append(item)

		# Generate CSV file
		tmpl = get_template('item/item_csv.csv')
		context = template.Context({'items': items})
		csv = tmpl.render(context)

		# Email user with CSV file
		email = EmailMessage(
			'Item Information',
			'Hi There,\n\nFind attached csv containing item information',
			'nepcoreserver@gmail.com',
			[data['toEmail']])
		email.attach('test.csv',csv,'text/csv')
		try:
			email.send()
			return JsonResponse({'msg': 'Successfully sent email'}, status=200)
		except:
			return JsonResponse({'msg': 'Something went wrong.\n\nMake sure you have entered a valid email address'}, status=400)

class GetItemView(TemplateView):
	template_name = "item/items.html"

	def get(self, request, itemPK):
		item = HandleItems.get_item_values(itemPK)
		return JsonResponse(item, status=200)