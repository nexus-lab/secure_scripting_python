import subprocess
import os
import sys	
from subprocess import check_output
MASTER="MasterList"

if os.path.isfile(MASTER):
	print ("$MASTER exists; please delete it") #1>&2
	sys.exit(1)
else:
	open(MASTER,"w")

for root, dirs, files in os.walk("."):
	for filename in files:
		if (not os.path.isfile(filename)) or filename+"x" == MASTER+"x":
			continue
		else:
			output1 = check_output(["ls", "-sail", filename])    ## for Linux
			## output1 = check_output(["dir", filename]) ## for Windows
			output2 = check_output(["shasum",filename])          ## for Linux
			## output2 = check_output(["certutil -hashfile",'"', filename, '"']) ## for Windows
			print (output1+" "+output2)
