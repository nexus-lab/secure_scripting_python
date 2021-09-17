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
