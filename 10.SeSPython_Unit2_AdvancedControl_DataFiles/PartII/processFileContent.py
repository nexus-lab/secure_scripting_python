myFile = open("dict.txt",'r')
for word in myFile:
	print(word.strip())