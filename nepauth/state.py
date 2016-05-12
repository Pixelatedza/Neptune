from nepcore.state import StateObj, state_manager

permissions = state_manager.register(StateObj(name="permissions", link='/nepcore/auth/'))
