import sys
if len(sys.argv) != 3:
	print("Usage: give exactly 3 argument, the string to be looked for")
else:
	with open(sys.argv[2]) as f:
		for line in f:
			if sys.argv[1] in line:
				print(line)
