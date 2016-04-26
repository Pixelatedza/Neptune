from nepcore import forms as nepForms # classes
from django import forms # fields and widgets

class ItemTypeForm(nepForms.NEPForm):
	itmeType = forms.CharField(max_length=50, label='Name')
	attrName = forms.CharField(max_length=50, label='Name')
	attrDataType = forms.CharField(max_length=50, label='Data Type')