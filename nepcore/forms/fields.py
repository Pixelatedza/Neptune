from django.forms import fields
from nepcore.forms.widgets import *

# This maps our dataTypes to django form fields
CUSTOM_FIELD_MAP = {
	"str": fields.CharField,
	"int": fields.IntegerField,
	"dat": fields.DateField,
	"tim": fields.TimeField
}