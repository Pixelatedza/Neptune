from django import forms

class ItemTypeForm(forms.Form):
    item_type = forms.CharField(label='item type', max_length=100)
    attributes = forms.CharField(label='attr', widget=forms.Textarea)