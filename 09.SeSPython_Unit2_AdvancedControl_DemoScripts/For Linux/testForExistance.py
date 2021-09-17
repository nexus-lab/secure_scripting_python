import os

X="MasterList.txt"
if( os.path.isfile(X) ):
	print ("File ",X," exists")
else:
	print("File ",X," does not exist")
