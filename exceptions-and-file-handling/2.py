# Bind the name getpass to the appropriate function

try:
	import termios, THERMIOS
except ImportError:
	try:
		import msvcrt
	except ImportError:
		try:
			from EasyDialogs import Askpassword
		except ImportError:
			getpass = default_getpass
		else:
			getpass = AskPassword
	else:
		getpass = win_getpass
else:
	getpass = unix_getpass
