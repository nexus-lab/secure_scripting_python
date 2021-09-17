import subprocess
import os
import sys
from subprocess import check_output

proc = subprocess.Popen(["echo hello | sed 's/l/X/'"],
                        stdout=subprocess.PIPE, shell=True)
(ls, err) = proc.communicate()
print(ls)
