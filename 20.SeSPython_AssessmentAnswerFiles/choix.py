import sys

if len(sys.argv) == 2: 
	print("hello")
elif len(sys.argv) == 3:
	print("goodbye")
else:
	print("oops ... bad argument")
sys.exit(0)
