import subprocess
import os
import sys	
from subprocess import check_output

MASTER="MasterList"
processID = str(os.getpid())
TMP=r"tmp"+processID+".txt"
tmpFile = open(TMP,'w')
tmpFile.close()

if not os.path.isfile(MASTER):
	print ("Master file does not exist; please generate it")
	sys.exit(1)

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

print("Changed files:")
proc3 = subprocess.Popen(["powershell.exe","fc.exe", MASTER, TMP], stdout=subprocess.PIPE, shell=True)
(fc, err) = proc3.communicate()
print(fc.rstrip().decode("utf-8"))

proc4 = subprocess.Popen(["del", TMP],stdout = subprocess.PIPE, shell=True)
(delete, err) = proc4.communicate()