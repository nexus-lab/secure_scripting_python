f = open('connect2.csv', 'r')
while f.readline():
    line = f.readline()
    print(line.strip())
f.close()
#    filedata = file.read()
#    # Replace the target string
#    filedata = filedata.replace(',', ' ')
#
#    # Write the file out again
# 	with open('connect3.csv', 'w') as file:
# 	file.write(filedata)
