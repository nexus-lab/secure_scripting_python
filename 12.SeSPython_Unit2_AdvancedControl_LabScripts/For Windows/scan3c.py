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
		if filename.startswith("tmp"):
			continue
		else:
			proc = subprocess.Popen(["powershell.exe", r"dir .\sample\{}".format(filename)],
									stdout=subprocess.PIPE, shell=True)
			(dir, err) = proc.communicate()
			proc = subprocess.Popen(["powershell.exe", r"certutil -hashfile .\sample\{}".format(filename)],
									stdout=subprocess.PIPE, shell=True)
			(sha, err) = proc.communicate()
			f = open(TMP, 'a')
			f.write(str(dir.rstrip().decode("utf-8")))
			f.writelines("\n")
			f.write(str(sha.rstrip().decode("utf-8")))
			f.close()