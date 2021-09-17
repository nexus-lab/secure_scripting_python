import subprocess
import sys
from subprocess import check_output

if len(sys.argv) != 2:
    print("Usage: give exactly 1 argument, the String to be looked for")
else:
    try:
        output = check_output(['grep', sys.argv[1], 'dict.txt']).decode("utf-8")
        print(output)
    except subprocess.CalledProcessError:
        print("String not found.")
