from nepcore.state import StateObj, state_manager

create_item_type_state = state_manager.register(StateObj(name="create_item_type_state", link='/nepcore/item/create/item-type/'))
item_state = state_manager.register(StateObj(name="item_type_state", link='/nepcore/item/'))
create_item_state = state_manager.register(StateObj(name="create_item_state", url="create_item_state/:itemName", link='/nepcore/item/create/', params=True))
