from nepcore import forms as nepForms # classes
from django import forms # fields and widgets

class ItemTypeForm(nepForms.NEPForm):
	itemType = forms.CharField(max_length=50, label='Name')

class ItemForm(nepForms.NEPForm):
	pass