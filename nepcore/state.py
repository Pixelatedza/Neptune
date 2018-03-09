import sys
from django.apps import apps
from django.conf import settings
from importlib import import_module, reload
from nepcore.models import NEPState

class StateManager(object):
	def __init__(self, *args, **kwargs):
		self.states = {}

	def auto_discover(self):
		for app in apps.get_app_configs():
			try:
				mod = '%s.%s' % (app.name, "state")
				if mod not in sys.modules:
					import_module(mod)
				elif mod != 'nepcore.state':
					reload(sys.modules[mod])
			except ImportError:
				pass
			except Exception as e:
				raise e
			
	def _get_states_from_db(self):
		states = NEPState.objects.all()
		for state in states:
			self.register(StateObj(name=state.name, url=state.url, link=state.link, params=state.params))

	def register(self, state):
		self.states[state.name] = state
		return state

	def states_to_json(self):
		jsonStates = []
		self.states = {}
		index_state = state_manager.register(StateObj(name="nep_index", link="/nepcore/index/"))
		self.auto_discover()
		self._get_states_from_db()
		for name, state in self.states.items():
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
# state_manager.auto_discover()