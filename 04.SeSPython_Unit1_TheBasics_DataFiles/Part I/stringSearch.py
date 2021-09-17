import sys
myString = "this is a text with several words"
target = sys.argv[1]
if(target in myString):
	print(target," was found!") 
else:
	print(target," was NOT found!")