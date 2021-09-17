
import sys

with open("dict.txt") as f:
	for line in f:
		if "gry" in line:
			print(line)
