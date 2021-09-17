import subprocess

proc = subprocess.Popen([r"echo 'hello there' | sed 's/.*\(.*\) /\1/'"], shell=True)
(ls, err) = proc.communicate()

