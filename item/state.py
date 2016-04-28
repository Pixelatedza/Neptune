from nepcore.state import StateObj, state_manager

create_item_type_state = state_manager.register(StateObj(name="item_type_state", link='/nepcore/item/create/item-type/'))
create_item_state = state_manager.register(StateObj(name="item_state", link='/nepcore/item/create/'))