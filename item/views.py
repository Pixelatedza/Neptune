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
		d['item_type'] = form.data['item_type']
		d['properties'] = []
		properties = form.data['properties'].split(',')
		for p in properties:
			li = p.split('-')
			d['properties'].append({'label':li[0],'_type':li[1]})
		#d['properties'] = form.data['properties'].split(',')
		HandleItems.create_type_with_props(d)
		return super(ItemTypeView, self).form_valid(form)

class ItemView(FormView):
	template_name = "item/dev.html"
	form_class = ItemTypeForm
	success_url = '/nepcore/item/'

	def form_valid(self, form):
		#print form.data
		d = {}
		d['item_type'] = form.data['item_type']
		d['properties'] = []
		properties = form.data['properties'].split(',')
		for p in properties:
			li = p.split('-')
			d['properties'].append({'label':li[0],'_type':li[1]})
		#d['properties'] = form.data['properties'].split(',')
		tempf(d)
		return super(IndexView, self).form_valid(form)