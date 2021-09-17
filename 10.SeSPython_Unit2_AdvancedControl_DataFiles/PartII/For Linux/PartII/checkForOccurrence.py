myFile = open("dict.txt",'r')
for word in myFile:
	if 'gry' in word:
		print(word.strip())