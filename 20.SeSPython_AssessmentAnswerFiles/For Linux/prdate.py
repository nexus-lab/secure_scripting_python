import sys
import os
import subprocess
from subprocess import check_output

mydate = check_output(["date"])

print("It is now", mydate)
sys.exit(0)
