import sys
from django.apps import apps
from django.conf import settings
from django.template.loader import get_template
from django import template
from django.utils.safestring import mark_safe
from importlib import import_module, reload
from nepcore.state import index_state
from nepcore.models import NEPMenu

class Menu(object):
	template_path = 'nepcore/menus/menu.html'
	location = 'main_nav'

	def __init__(self, *args, **kwargs):
		self.children = {}
		self.parent = kwargs.get('menu', None)
		self.icon = kwargs.get('icon', None)

	def build_menu(self, request=None):
		# this is a mess, must make menus dynamic
		self.request = request
		self.children = {}
		menu.register(text='Welcome to Neptune', state=index_state)
		self._build_from_modules()
		self._build_from_db()
			
	def _build_from_modules(self):
		# Still not sure if this is the right way, but it sure works a charm!
		for app in apps.get_app_configs():
			try:
				mod = '%s.%s' % (app.name, "menu")
				print(mod)
				if mod not in sys.modules:
					import_module(mod)
				elif mod != 'nepcore.menu':
					reload(sys.modules[mod])
			except ImportError:
				pass
			except Exception as e:
				raise e
			
	def _build_from_db(self, query=NEPMenu.objects.filter(parent=None)):
		#qs = NEPMenu.objects.filter(parent=None)
		for menu in query:
			self.register(icon=menu.icon, link=menu.link, parent=menu.parent, state=menu.state, text=menu.text)
			self._build_from_db(menu.menus.all())

	def register(self, *args, **kwargs):
		menu_obj = kwargs.get('menu_obj', None)
		if not menu_obj:
			menu_obj = MenuObj(**kwargs)
		menu_obj.parent = self
		self.children[menu_obj.text] = menu_obj
		return menu_obj

	def render(self):
		tmpl = get_template(self.template_path)
		html = tmpl.render({'menu': self})
		return html

	def __str__(self):
		return self

class MenuObj(Menu):
	template_path = 'nepcore/menus/menu_obj.html'

	def __init__(self, *args, **kwargs):
		super(MenuObj, self).__init__(*args, **kwargs)
		self.state = kwargs.get('state', None)
		self.text = kwargs.get('text', 'Menu')
		self.link = kwargs.get('link', None)

	def __str__(self):
		return self.text

menu = Menu()