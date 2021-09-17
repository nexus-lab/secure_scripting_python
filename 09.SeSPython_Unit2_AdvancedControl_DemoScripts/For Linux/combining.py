  
import subprocess
proc = subprocess.Popen(['ls -l combining.py'],
                        stdout = subprocess.PIPE, shell=True)
(ls, err) = proc.communicate()
proc = subprocess.Popen(['shasum combining.py'],
                         stdout = subprocess.PIPE, shell=True)
(sha, err) = proc.communicate()
print (ls.rstrip()," ",sha.rstrip())

