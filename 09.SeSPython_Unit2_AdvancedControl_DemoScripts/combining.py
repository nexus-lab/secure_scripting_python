  
import subprocess

proc = subprocess.Popen(["dir","-n", "dict.txt"], stdout = subprocess.PIPE, shell=True)
(directory, err) = proc.communicate()

proc = subprocess.Popen(["certutil", "-hashfile", "dict.txt"], stdout = subprocess.PIPE, shell=True)
(sha, err) = proc.communicate()

print(directory.rstrip().decode("utf-8"),"\n",sha.rstrip().decode("utf-8"))
