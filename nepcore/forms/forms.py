from nepcore.forms.fields import *
from django.utils import six
from django.forms.forms import BoundField, DeclarativeFieldsMetaclass
from django.forms import BaseForm, Textarea
from django.utils.html import format_html

class NEPBoundField(BoundField):
	def label_tag(self, contents=None, attrs=None, label_suffix=None):
		attrs = {'class':'col-xs-2 control-label'}
		return 'ng-class={"has-error":formErrors["' + self.name + '"]}>' + super(NEPBoundField, self).label_tag(contents, attrs, label_suffix)

	def as_widget(self, widget=None, attrs=None, only_initial=False):
		attrs = {'class':'form-control', 'ng-model':'formData["' + self.name + '"]'}
		error_html = """<div ng-class="{'bg-red color-palette nep-error':formErrors.""" + self.name + """}">
			<span>{[{formErrors[\"""" + self.name + """\"]}]}</span>
		</div>"""
		return super(NEPBoundField, self).as_widget(widget, attrs, only_initial) + error_html

class NEPBaseForm(BaseForm):

	def __getitem__(self, name):
		"Returns a NEPBoundField with the given name. A NEPBoundField is a customized field for NEPCORE"
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
			normal_row='<div class="row form-group"%(label)s<div class="col-xs-10">%(errors)s%(field)s%(help_text)s</div></div>',
			error_row='<tr><td colspan="2">%s</td></tr>',
			row_ender='</td></tr>',
			help_text_html='<br /><span class="helptext">%s</span>',
			errors_on_separate_row=False)

	def _html_output(self, normal_row, error_row, row_ender, help_text_html, errors_on_separate_row):
		return super(NEPBaseForm, self)._html_output(normal_row, error_row, row_ender, help_text_html, errors_on_separate_row)

class NEPForm(six.with_metaclass(DeclarativeFieldsMetaclass, NEPBaseForm)):
	"This is the main form class for neptune forms."
	# The following was pulled from djangos Form class. I followed their ways.
	#
	# This is a separate class from BaseForm in order to abstract the way
	# self.fields is specified. This class (Form) is the one that does the
	# fancy metaclass stuff purely for the semantic sugar -- it allows one
	# to define a form using declarative syntax.
	# BaseForm itself has no way of designating self.fields.