import os
try:
	virtual_env = os.environ["VIRTUAL_ENV"]
	print (f"Virtual environment variable: {virtual_env}")
except KeyError:
	print ("We are NOT in the virtual environment!")