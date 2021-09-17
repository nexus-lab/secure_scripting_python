import subprocess
import os
import sys	
from subprocess import check_output

MASTER="MasterList"
processID = str(os.getpid())
TMP="/tmp/"+processID+".txt"
tmpFile = open(TMP,'w')

for root, dirs, files in os.walk("sample"):
	for filename in files:
		if filename == tmpFile:
			continue
		else:
			proc = subprocess.Popen(["ls -sail sample/" + filename], stdout=subprocess.PIPE, shell=True)
			(ls, err) = proc.communicate()

			proc = subprocess.Popen(["shasum sample/" + filename], stdout=subprocess.PIPE, shell=True)
			(sha, err) = proc.communicate()
			f = open(MASTER, 'a')
			f.write(str(ls.rstrip()))
			f.writelines('\n')
			f.write(str(sha.rstrip()))
			f.writelines('\n')
			f.close()

proc = subprocess.Popen(["diff "+MASTER+" "+TMP],stdout = subprocess.PIPE, shell=True)
(diff, err) = proc.communicate()
print (diff)

proc = subprocess.Popen(["rm "+TMP],stdout = subprocess.PIPE, shell=True)
(rm, err) = proc.communicate()