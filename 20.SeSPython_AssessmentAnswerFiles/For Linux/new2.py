import sys

if len(sys.argv)-1 != 3:
	print("Usage: "+sys.argv[0]+" num1 num2 [ -m | -d ]")
	sys.exit(1)
if sys.argv[3] == "-m":
	print(int(sys.argv[1]) * int(sys.argv[2]))
elif sys.argv[3] == "-d":
	print(int(sys.argv[1]) / int(sys.argv[2]))
else:
	print(sys.argv[0]+": third argument must be -m or -d")
	sys.exit(1)
sys.exit(0)
