import sys
if len(sys.argv) != 3:
	print("Usage: lookfor4 string file")
else:
	with open(sys.argv[2]) as f:
		for line in f:
			if sys.argv[1] in line:
				print(line)
