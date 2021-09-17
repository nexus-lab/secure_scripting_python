import time
import datetime
import os

print("Time in seconds since the epoch: %s" % time.time())
now = datetime.datetime.now()
print(now.strftime("%a %b %d %H:%M:%S %Z %Y"))

print("or using the system call")
os.system("date")
