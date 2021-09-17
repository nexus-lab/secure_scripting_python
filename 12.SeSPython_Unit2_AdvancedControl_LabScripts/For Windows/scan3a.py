import subprocess
import os
import sys	
from subprocess import check_output

MASTER="MasterList"
processID = str(os.getpid())
TMP=r"tmp"+processID+".txt"
tmpFile = open(TMP,'w')
tmpFile.close()

for root, dirs, files in os.walk("sample"):
	for filename in files:
		proc = subprocess.Popen(["powershell.exe", r"dir .\sample\{}".format(filename)], stdout=subprocess.PIPE, shell=True)
		(dir, err) = proc.communicate()
		proc2 = subprocess.Popen(["powershell.exe", r"certutil -hashfile .\sample\{}".format(filename)], stdout=subprocess.PIPE, shell=True)
		(shasum, err) = proc2.communicate()
		print (dir.rstrip().decode("utf-8"), shasum.rstrip().decode("utf-8"))
