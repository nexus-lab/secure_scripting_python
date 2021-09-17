import subprocess

proc = subprocess.Popen(["date","/t"], stdout = subprocess.PIPE, shell=True)
(date, err) = proc.communicate()

proc = subprocess.Popen(["whoami"], stdout = subprocess.PIPE, shell=True)
(who, err) = proc.communicate()


print("at ",date.rstrip().decode("utf-8")," i was ",who.rstrip().decode("utf-8"))

