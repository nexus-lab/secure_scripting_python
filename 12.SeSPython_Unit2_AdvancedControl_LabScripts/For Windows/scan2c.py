import subprocess
import os
import sys	
from subprocess import check_output
MASTER="MasterList"

if os.path.isfile(MASTER):
	print ("$MASTER exists; please delete it")
	sys.exit(1)
else:
	open(MASTER,"w")

for root, dirs, files in os.walk("sample"):
	for filename in files:
		if filename == MASTER:
			continue
		else:
			proc = subprocess.Popen(["powershell.exe", r"dir .\sample\{}".format(filename)],
									stdout=subprocess.PIPE, shell=True)
			(dir, err) = proc.communicate()
			proc = subprocess.Popen(["powershell.exe", r"certutil -hashfile .\sample\{}".format(filename)],
									stdout=subprocess.PIPE, shell=True)
			(sha, err) = proc.communicate()
			print()
			print(dir.rstrip().decode("utf-8"))
			print(sha.rstrip().decode("utf-8"))
