import subprocess
import os
import sys	
from subprocess import check_output

MASTER="MasterList"
processID = str(os.getpid())
TMP="/tmp/"+processID+".txt"
tmpFile = open(TMP,'w')

for r, d, f in os.walk("sample"):
	for fi in f:
		proc = subprocess.Popen(["ls -sail sample/" + fi], stdout=subprocess.PIPE, shell=True)
		(ls, err) = proc.communicate()

		proc = subprocess.Popen(["shasum sample/" + fi], stdout=subprocess.PIPE, shell=True)
		(sha, err) = proc.communicate()
		print(ls.rstrip().decode("utf-8"), sha.rstrip().decode("utf-8"))
