from nepcore.state import StateObj, state_manager

create_item_type_state = state_manager.register(StateObj(name="create_item_type_state", link='/item/create/item-type/'))
item_state = state_manager.register(StateObj(name="item_type_state", link='/item/'))
create_edit_item_state = state_manager.register(StateObj(name="create_edit_item_state", url=":url", link='/item/create/', params=True))
