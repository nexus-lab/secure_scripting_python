import os

X="MasterList"
if( os.path.isfile(X) ):
	print("File ",X," exists")
else:
	print ("File ",X," does not exist")
