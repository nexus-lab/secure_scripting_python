from subprocess import check_output
output = check_output(["findstr", "gry", "dict.txt"], shell=True).decode("utf-8")
print(output)


import sys
from subprocess import check_output

output = check_output(["type", sys.argv[1]], shell=True).decode("utf-8")
print(output)
