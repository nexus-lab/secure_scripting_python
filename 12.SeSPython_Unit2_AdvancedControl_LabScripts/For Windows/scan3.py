import subprocess
import os
import sys	
from subprocess import check_output

MASTER="MasterList"
processID = str(os.getpid())
TMP="tmp"+processID+".txt"
tmpFile = open(TMP,'w')
tmpFile.close()

for root, dirs, files in os.walk("."):
	for filename in files:
		if filename == tmpFile:
			continue
		else:
			proc = subprocess.Popen(["dir", "/n", filename], stdout=subprocess.PIPE, shell=True)
			(dir, err) = proc.communicate()
			proc2 = subprocess.Popen(["certutil", "-hashfile", filename], stdout=subprocess.PIPE, shell=True)
			(shasum, err) = proc2.communicate()
			f = open(MASTER, 'a')
			f.write(dir.rstrip().decode("utf-8") + "\n" + shasum.rstrip().decode("utf-8"))
			f.close()

print ("Changed files:")
proc3 = subprocess.Popen(["fc", MASTER, TMP],stdout = subprocess.PIPE, shell=True)
(fc, err) = proc3.communicate()
print (fc.rstrip().decode("utf-8"))

proc4 = subprocess.Popen(["del", TMP],stdout = subprocess.PIPE, shell=True)
(delete, err) = proc4.communicate()