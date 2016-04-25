from django.forms import widgets

class NEPTextAreaNoResize(widgets.Textarea):
	
	def __init__(self, attrs=None):
		super(NEPTextArea, self).__init__(attrs={'style="resize: none"'})