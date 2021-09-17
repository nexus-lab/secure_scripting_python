import os

for root, dirs, files in os.walk("."):
	for filename in files:
		print("file name: ",filename)
