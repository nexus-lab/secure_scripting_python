import subprocess
import os
import sys
from subprocess import check_output

# exercise 2a
MASTER="MasterList"

GENMASTER = "no"
DELMASTER = "no"
try:
	if sys.argv[1] == '-g':
		GENMASTER = "yes"
	if sys.argv[1] == '-d':
		DELMASTER = "yes"
	if sys.argv[1] != '-g' or sys.argv[1] != '-d':
		print("Unknown option: " + sys.argv[1])
		sys.exit(1)
except IndexError:
	pass

if GENMASTER == 'yes':
	MASTER = "MasterList"

	if os.path.isfile(MASTER):
		print("$MASTER exists; please delete it")  # 1>&2
		sys.exit(1)
	else:
		open(MASTER, "w")

	for root, dirs, files in os.walk("sample"):
		for filename in files:
			if filename + "x" == MASTER + "x":
				continue
			else:
				proc = subprocess.Popen(["powershell.exe", r"dir .\sample\{}".format(filename)],
										stdout=subprocess.PIPE, shell=True)
				(dir, err) = proc.communicate()
				proc = subprocess.Popen(["powershell.exe", r"certutil -hashfile .\sample\{}".format(filename)],
										stdout=subprocess.PIPE, shell=True)
				(sha, err) = proc.communicate()
				f = open(MASTER, 'a')
				f.write(str(dir.rstrip().decode("utf-8")))
				f.writelines("\n")
				f.write(str(sha.rstrip().decode("utf-8")))
				f.close()
	sys.exit(0)



# exercise 3a
processID = str(os.getpid())
TMP="tmp"+processID+".txt"
tmpFile = open(TMP,"w")
tmpFile.close()

# exercise 3e
if not os.path.isfile(MASTER):
	print ("Master file does not exist; please generate it")
	sys.exit(1)

for root, dirs, files in os.walk("sample"):
	for filename in files:

		# exercise 3b
		if filename.startswith("tmp"):
			continue
		# exercise 2c
		if filename+"x" == MASTER+"x":
			continue
		# exercise 3c
		proc = subprocess.Popen(["powershell.exe", r"dir .\sample\{}".format(filename)],
								stdout=subprocess.PIPE, shell=True)
		(dir, err) = proc.communicate()
		proc = subprocess.Popen(["powershell.exe", r"certutil -hashfile .\sample\{}".format(filename)],
								stdout=subprocess.PIPE, shell=True)
		(sha, err) = proc.communicate()
		f = open(TMP, 'a')
		f.write(str(dir.rstrip().decode("utf-8")))
		f.writelines("\n")
		f.write(str(sha.rstrip().decode("utf-8")))
		f.close()

# exercise 3d, with the modification given in exercise 4
print ("Changed files:")
proc3 = subprocess.Popen(["fc", MASTER, TMP],stdout = subprocess.PIPE, shell=True)
(fc, err) = proc3.communicate()
print (fc.rstrip().decode("utf-8"))
# exercise 3f
proc4 = subprocess.Popen(["del", TMP],stdout = subprocess.PIPE, shell=True)
(delete, err) = proc4.communicate()
