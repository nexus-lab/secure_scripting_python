import sys

if len(sys.argv)-1 == 0:
	print("No arguments given")
elif sys.argv[1] == "":
	print("The argument is empty")
else:
	print(sys.argv[1])
sys.exit(0)
