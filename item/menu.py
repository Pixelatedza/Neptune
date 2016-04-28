from nepcore.menu import menu
from item.state import *

itemType = menu.register(text="Item Types (temp)",state=create_item_type_state)
item = menu.register(text="Items (temp)",state=create_item_state)