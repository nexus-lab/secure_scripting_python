import os
import sys
FILE = input("Name of File: ")
if( FILE != "gleep" and not os.path.isfile(FILE)):
	print("not gleep, and a regular file")
sys.exit(0)
