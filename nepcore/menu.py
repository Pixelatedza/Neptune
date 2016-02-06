from django.conf import settings
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from importlib import import_module
from django import template

class Menu(object):
	template_path = 'nepcore/menus/menu.html'

	def __init__(self, *args, **kwargs):
		self.children = []
		self.parent = kwargs.get('menu', None)
		self.location = kwargs.get('location', None)

	def auto_discover(self):
		for app in settings.INSTALLED_APPS:
			try:
				import_module('%s.%s' % (app, "menu"))
			except ImportError:
				pass
			except Exception as e:
				raise e

	## TODO
	# Change params to args, kwargs and create the menu_obj in this function.
	# This will allow other modules to use register without having to import
	# the MenuObj class.
	def register(self, menu_obj):
		menu_obj.parent = self
		self.children.append(menu_obj)
		return menu_obj

	def render(self):
		template = get_template(self.template_path)
		return template.render()

	def __str__(self):
		return self.render()

class MenuObj(Menu):

	def __init__(self, *args, **kwargs):
		super(MenuObj, self).__init__(*args, **kwargs)
		self.link = kwargs.get('link', '')
		self.text = kwargs.get('text', 'Menu')

	def __str__(self):
		return self.text

menu = Menu(location="main_nav")
hello_menu = menu.register(MenuObj(link="hello",text="Hello Menu"))
hello_menu.register(MenuObj(link="child 1",text="Child 1"))
hello_menu.register(MenuObj(link="child 2",text="Child 2"))
other_menu = menu.register(MenuObj(link="other",text="Other Menu"))

menu.auto_discover()