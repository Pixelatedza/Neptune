from nepcore import forms as nepForms # classes
from django import forms # fields and widgets
from neplist.models import Check

class CheckForm(nepForms.NEPForm):
	checkPk = forms.IntegerField(widget=forms.HiddenInput())
	status = forms.IntegerField(widget=forms.HiddenInput())
	proof_file = forms.FileField()
#	status = forms.ChoiceField(choices=Check.STATUS_CHOICES)