from django.conf import settings
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from importlib import import_module
from django import template

class Menu(object):
	template_path = 'nepcore/menus/menu.html'
	location = 'main_nav'

	def __init__(self, *args, **kwargs):
		self.children = []
		self.parent = kwargs.get('menu', None)
		self.icon = kwargs.get('icon', None)

	def auto_discover(self):
		for app in settings.INSTALLED_APPS:
			try:
				import_module('%s.%s' % (app, "menu"))
			except ImportError:
				pass
			except Exception as e:
				raise e

	def register(self, *args, **kwargs):
		menu_obj = kwargs.get('menu_obj', None)
		if not menu_obj:
			menu_obj = MenuObj(**kwargs)
		menu_obj.parent = self
		self.children.append(menu_obj)
		return menu_obj

	def render(self):
		tmpl = get_template(self.template_path)
		context = template.Context({'menu': self})
		html = tmpl.render(context)
		return html

	def __str__(self):
		return self.render()

class MenuObj(Menu):
	template_path = 'nepcore/menus/menu_obj.html'

	def __init__(self, *args, **kwargs):
		super(MenuObj, self).__init__(*args, **kwargs)
		self.link = kwargs.get('link', '')
		self.text = kwargs.get('text', 'Menu')

	def __str__(self):
		return self.text

menu = Menu()
menu.register(link="db", text="Dashboard", icon="dashboard")
menu.auto_discover()