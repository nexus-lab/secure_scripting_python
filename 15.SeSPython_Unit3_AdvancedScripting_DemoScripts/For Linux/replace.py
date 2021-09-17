import subprocess

proc = subprocess.Popen(["echo hello | sed 's/l/X/'"], shell=True)
(ls, err) = proc.communicate()
