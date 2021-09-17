import subprocess
import os
import sys	
from subprocess import check_output
proc = subprocess.Popen(["echo 'hello there' | sed -f 's/.* \(.*\)/\1/'"],
       stdout = subprocess.PIPE, shell=True)
(cmd, err) = proc.communicate()
print cmd
