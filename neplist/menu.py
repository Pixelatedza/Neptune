from nepcore.menu import menu
from neplist.state import *

main = menu.register(text="Lists")
main.register(text="Worklists", state=index)
