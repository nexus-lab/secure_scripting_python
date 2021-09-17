import sys

with open("dict.txt") as f:
	for line in f:
		if sys.argv[2] in line:
			print(line)
