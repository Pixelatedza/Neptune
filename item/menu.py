from nepcore.menu import menu
from item.state import *

items= menu.register(text="Items",state=item_state)
itemTypes = menu.register(text="ItemTypes",state=create_item_type_state)