import sys

DELMASTER = False
GENMASTER = False
print(len(sys.argv))
for i in range(1,len(sys.argv)):
	if sys.argv[i] == "-d":
		DELMASTER = True
	elif sys.argv[i] == "-g":
		GENMASTER = True
	else:
		print(sys.argv[i]," is not a valid option")
		sys.exit(1)
