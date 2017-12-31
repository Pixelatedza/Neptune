from django.apps import apps
from django.conf import settings
from importlib import import_module

class StateManager(object):
	def __init__(self, *args, **kwargs):
		self.states = []

	def auto_discover(self):
		for app in apps.get_app_configs():
			try:
				import_module('%s.%s' % (app.name, "state"))
			except ImportError:
				pass
			except Exception as e:
				raise e

	def register(self, state):
		self.states.append(state)
		return state

	def states_to_json(self):
		jsonStates = []
		for state in self.states:
			jsonStates.append({
				"name": state.name,
				"url": state.url,
				"link": state.link,
				"params": state.params
			})
		return jsonStates

	def __str__(self):
		return self

class StateObj(StateManager):

	def __init__(self, *args, **kwargs):
		super(StateObj, self).__init__(*args, **kwargs)
		self.name = kwargs.get('name', None)
		self.url = kwargs.get('url', self.name)
		self.link = kwargs.get('link', None)
		self.params = kwargs.get('params', None)

	def __str__(self):
		return self.name

state_manager = StateManager()
index_state = state_manager.register(StateObj(name="nep_index", link="/nepcore/index/"))
state_manager.auto_discover()