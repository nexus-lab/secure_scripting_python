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
except IndexError:
	pass

#Generates Masterlist if option is given
if GENMASTER=="yes":
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
				proc = subprocess.Popen(["ls -sail sample/" + filename], stdout=subprocess.PIPE, shell=True)
				(ls, err) = proc.communicate()

				proc = subprocess.Popen(["shasum sample/" + filename], stdout=subprocess.PIPE, shell=True)
				(sha, err) = proc.communicate()
				f = open(MASTER, 'a')
				f.write(str(ls.rstrip().decode("utf-8")))
				f.writelines('\n')
				f.write(str(sha.rstrip().decode("utf-8")))
				f.writelines('\n')
				f.close()
	sys.exit(0)

# exercise 3a
processID = str(os.getpid())
TMP="/tmp/"+processID+".txt"
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
		else:
			proc = subprocess.Popen(["ls -sail sample/" + filename], stdout=subprocess.PIPE, shell=True)
			(ls, err) = proc.communicate()

			proc = subprocess.Popen(["shasum sample/" + filename], stdout=subprocess.PIPE, shell=True)
			(sha, err) = proc.communicate()
			f = open(TMP, 'a')
			f.write(str(ls.rstrip().decode("utf-8")))
			f.writelines('\n')
			f.write(str(sha.rstrip().decode("utf-8")))
			f.writelines('\n')
			f.close()

# exercise 3d, with the modification given in exercise 4
print("Changed files:")
proc = subprocess.Popen(["diff " + MASTER + " " + TMP], stdout=subprocess.PIPE, shell=True)
(diff, err) = proc.communicate()
print(diff.rstrip().decode("utf-8"))
# exercise 3f
proc = subprocess.Popen(["rm "+TMP],stdout = subprocess.PIPE, shell=True)
(rm, err) = proc.communicate()
sys.exit(0)
