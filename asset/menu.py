from nepcore.menu import MenuObj, hello_menu, menu

menu = menu.register(MenuObj(link="hello asset",text="Hello Asset"))
hello_menu.register(MenuObj(link="child 1 asset",text="Child 1 Asset"))
hello_menu.register(MenuObj(link="child 2 asset",text="Child 2 Asset"))
