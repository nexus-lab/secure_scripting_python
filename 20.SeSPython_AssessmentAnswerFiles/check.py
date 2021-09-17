import os
import sys
if os.path.isfile("MasterList"):
	print("MasterList exists")
	sys.exit(0)
else:
	print("MasterList: no such file")
	sys.exit(1)
