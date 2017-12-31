from nepcore.menu import menu
from nepauth.state import *

if menu.request.user.has_perm('auth.change_permission'):
	main = menu.register(text="Permissions",state=permissions)
