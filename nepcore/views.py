from django.views.generic import TemplateView
from nepcore.menu import menu

class IndexView(TemplateView):
	template_name = "nepcore/index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['menu'] = menu
		return context
