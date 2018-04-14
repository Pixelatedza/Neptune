from nepcore.state import StateObj, state_manager

index = state_manager.register(StateObj(name="list", link='/nepcore/list/'))
checklist = state_manager.register(StateObj(name="checklist", url=':url', link='/nepcore/list/checklist/', params=True))
