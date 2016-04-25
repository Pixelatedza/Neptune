from nepcore.forms.fields import *
from django.forms.forms import BoundField
from django.forms import ModelForm, Textarea
from django.utils.html import format_html
from asset.models import *

class NEPBoundField(BoundField):
	def label_tag(self, contents=None, attrs=None, label_suffix=None):
		attrs = {'class':'col-sm-2 control-label'}
		return super(NEPBoundField, self).label_tag(contents, attrs, label_suffix)

	def as_widget(self, widget=None, attrs=None, only_initial=False):
		attrs = {'class':'form-control'}
		return super(NEPBoundField, self).as_widget(widget, attrs, only_initial)

class NEPBaseModelForm(ModelForm):
	class Meta:
		exclude = ["pk"]
		widgets = {
			'comments': Textarea(attrs={'style':'resize: none'})
		}

	def __getitem__(self, name):
		"Returns a NEPBoundField with the given name. An NEPBoundField is a customized field for NEPCORE"
		try:
			field = self.fields[name]
		except KeyError:
			raise KeyError(
				"Key %r not found in '%s'" % (name, self.__class__.__name__))
		if name not in self._bound_fields_cache:
			self._bound_fields_cache[name] = NEPBoundField(self, field, name)
		return self._bound_fields_cache[name]

	def as_bootstrap(self):
		"Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
		return self._html_output(
			normal_row='<div class="form-group">%(label)s<div class="col-sm-10">%(errors)s%(field)s%(help_text)s</div></div>',
			error_row='<tr><td colspan="2">%s</td></tr>',
			row_ender='</td></tr>',
			help_text_html='<br /><span class="helptext">%s</span>',
			errors_on_separate_row=False)

	def _html_output(self, normal_row, error_row, row_ender, help_text_html, errors_on_separate_row):
		return super(NEPBaseModelForm, self)._html_output(normal_row, error_row, row_ender, help_text_html, errors_on_separate_row)