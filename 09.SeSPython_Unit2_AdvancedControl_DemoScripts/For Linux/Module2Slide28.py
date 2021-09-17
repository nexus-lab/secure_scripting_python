file = open("filename.txt","w") 
file.write("Hello World\n") 
file.close() 



file = open("filename.txt","a") 
file.write("This line only appends more text at the end of file") 
file.close()