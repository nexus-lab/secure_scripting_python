import subprocess
import sys
from subprocess import check_output
if len(sys.argv) != 2:
    print("Usage: give exactly 1 argument, the string to be looked for")
else:
    try:
        output = check_output(["findstr", sys.argv[1], "dict.txt"], shell=True).decode("utf-8")
        print(output)
    except subprocess.CalledProcessError:
        print("String not found.")
