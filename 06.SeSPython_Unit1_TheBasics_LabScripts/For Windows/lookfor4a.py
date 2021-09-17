import subprocess
import sys
from subprocess import check_output
if len(sys.argv) != 3:
    print("Usage: lookfor4 string file")
else:
    try:
        output = check_output(["findstr", sys.argv[1], sys.argv[2]], shell=True).decode("utf-8")
        print(output)
    except subprocess.CalledProcessError:
        print("String not found.")
