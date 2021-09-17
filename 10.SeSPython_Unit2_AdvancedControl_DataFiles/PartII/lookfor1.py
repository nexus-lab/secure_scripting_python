import sys
myFile = open("dict.txt", 'r')
for word in myFile:
	if(sys.argv[1] in word):
		print(word.strip())
