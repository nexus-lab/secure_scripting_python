import subprocess
import sys
from subprocess import check_output
try:
    output = check_output(["findstr", sys.argv[1], "dict.txt"], shell=True).decode("utf-8")
    print(output)
except subprocess.CalledProcessError:
    print("String not found.")
