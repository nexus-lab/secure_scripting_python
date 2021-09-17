import subprocess
import os
import sys	
from subprocess import check_output

MASTER="MasterList"
processID = str(os.getpid())
TMP="/tmp/"+processID+".txt"
tmpFile = open(TMP,'w')

for root, dirs, files in os.walk("."):
	for filename in files:
		if filename == tmpFile:
			continue
		else:
			output1 = check_output(["ls", "-sail", filename])
			output2 = check_output(["shasum",filename])
			print output1+" "+output2