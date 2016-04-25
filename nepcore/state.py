from django.conf import settings
from importlib import import_module

class StateManager(object):
	def __init__(self, *args, **kwargs):
		self.states = []

	def auto_discover(self):
		for app in settings.INSTALLED_APPS:
			try:
				import_module('%s.%s' % (app, "state"))
			except ImportError:
				pass
			except Exception as e:
				raise e

	def register(self, state):
		self.states.append(state)
		return state

	def __str__(self):
		return self

class StateObj(StateManager):

	def __init__(self, *args, **kwargs):
		super(StateObj, self).__init__(*args, **kwargs)
		self.name = kwargs.get('name', None)
		self.link = kwargs.get('link', None)

	def __str__(self):
		return self.name

state_manager = StateManager()
index_state = state_manager.register(StateObj(name="index", link="/nepcore/index/"))
state_manager.auto_discover()