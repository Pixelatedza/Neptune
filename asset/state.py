from nepcore.state import StateObj, state_manager

list_asset = state_manager.register(StateObj(name="list_asset", link='/nepcore/asset/list/'))
test = state_manager.register(StateObj(name="test", link='/nepcore/test/?model=Computer'))
