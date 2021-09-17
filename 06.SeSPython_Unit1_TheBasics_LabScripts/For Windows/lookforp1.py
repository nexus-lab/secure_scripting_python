import subprocess
import sys
from subprocess import check_output
if len(sys.argv) != 3:
    file_name = sys.argv[0]
    print("Usage:", file_name, "string file")
else:
    try:
        output = check_output(["findstr", sys.argv[1], sys.argv[2]], shell=True).decode("utf-8")
        print(output)
    except subprocess.CalledProcessError:
        print(sys.argv[0], ": file ", sys.argv[2], " cannot be read")
