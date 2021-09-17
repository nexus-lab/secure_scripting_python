import subprocess
import sys
from subprocess import check_output
try:
    output = check_output(['grep', sys.argv[1], 'dict.txt']).decode("utf-8")
    print(output)
except subprocess.CalledProcessError:
    print("String not found.")
