import subprocess
import os
import sys
from subprocess import check_output

proc = subprocess.Popen(["powershell.exe", "echo hello | %{$_ -replace 'l', 'X'}"])
proc.communicate()
