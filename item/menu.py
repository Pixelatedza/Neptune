from nepcore.menu import menu
from item.state import *

items = menu.register(text="Items",state=item_state)

if menu.request.user.has_perm('item.change_itemtype'):
	itemTypes = menu.register(text="ItemTypes",state=create_item_type_state)