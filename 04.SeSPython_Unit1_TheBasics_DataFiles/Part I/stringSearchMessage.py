import sys
myString = "this is a text with several words"

if len(sys.argv) != 2:
	print("Usage: give exactly 1 argument, the string to be looked for")
else:
	target = sys.argv[1]	
	if(target in myString):
		print(target," was found!") 
	else:
		print(target," was NOT found!")
