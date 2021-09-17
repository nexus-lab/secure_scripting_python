import subprocess
import os
import sys	
from subprocess import check_output
MASTER="MasterList"

if os.path.isfile(MASTER):
	print (MASTER ,"exists; please delete it") #1>&2
	sys.exit(1)
else:
	open(MASTER,"w")

for root, dirs, files in os.walk("sample"):
	for filename in files:
		if filename+"x" == MASTER+"x":
			continue
		else:
			proc = subprocess.Popen(["ls -sail sample/" + filename], stdout=subprocess.PIPE, shell=True)
			(ls, err) = proc.communicate()

			proc = subprocess.Popen(["shasum sample/" + filename], stdout=subprocess.PIPE, shell=True)
			(sha, err) = proc.communicate()
			print(ls.rstrip(), sha.rstrip())
