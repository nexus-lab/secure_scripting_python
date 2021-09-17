import sys
if len(sys.argv) != 2:
	print("Usage: give exactly 1 argument, the string to be looked for")
else:
	with open("dict.txt") as f:
		for line in f:
			if sys.argv[1] in line:
				print(line)
