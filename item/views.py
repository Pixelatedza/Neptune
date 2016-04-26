from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from item.forms import ItemTypeForm
from item.apps import HandleItems

def tempf(d):
	print d

class ItemTypeView(FormView):
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
			d['attributes'].append({'label':li[0],'dataType':li[1]})
		#d['attributes'] = form.data['attributes'].split(',')
		HandleItems.create_type_with_attrs(d)
		return super(ItemTypeView, self).form_valid(form)

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
		tempf(d)
		return super(IndexView, self).form_valid(form)