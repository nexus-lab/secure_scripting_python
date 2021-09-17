import sys
import os

for i in range(1,	len(sys.argv)):
	filename = sys.argv[i]
	if os.path.isfile(filename):
		print("File ",filename," exists")
	else:
		print("File ",filename," does not exist")
sys.exit(0)
