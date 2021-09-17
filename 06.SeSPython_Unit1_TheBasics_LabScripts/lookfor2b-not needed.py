import sys	
from subprocess import check_output
output = check_output(["findstr", sys.argv[2], sys.argv[1]],shell=True).decode("utf-8")
print(output)
