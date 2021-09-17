import sys
import os
import subprocess
from subprocess import check_output

mydate = subprocess.Popen('date /t', shell=True)
(output, errors) = mydate.communicate()

sys.exit(0)
