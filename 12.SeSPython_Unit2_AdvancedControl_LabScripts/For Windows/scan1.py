#
#if master file not there, create it
#
import subprocess
import os

for root, dirs, files in os.walk("sample"):
	for filename in files:
		proc = subprocess.Popen(["powershell.exe", r"dir .\sample\{}".format(filename)],
								stdout=subprocess.PIPE, shell=True)
		(dir, err) = proc.communicate()
		proc = subprocess.Popen(["powershell.exe", r"certutil -hashfile .\sample\{}".format(filename)],
								stdout=subprocess.PIPE, shell=True)
		(sha, err) = proc.communicate()
		print()
		print (dir.rstrip().decode("utf-8"))
		print(sha.rstrip().decode("utf-8"))
