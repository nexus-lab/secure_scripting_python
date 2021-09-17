import subprocess
import os
import sys	
from subprocess import check_output
MASTER="MasterList"

for r, d, f in os.walk("."):
	for fi in f:
		output1 = check_output(["ls", "-sail", fi])    #for Linux
		## output1 = check_output(["dir", fi])         #for Windows
		output2 = check_output(["shasum", fi])                             #for Linux
		## output2 = check_output(["certutil -hashfile",'"',fi,'"'])       #for Windows
		print (output1+" "+output2)