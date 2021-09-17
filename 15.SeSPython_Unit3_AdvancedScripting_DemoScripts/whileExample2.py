f = open("gleep", 'r')
line = f.readline()
while line:
    tokens = line.split()
    print(tokens[0], " is followed by ", tokens[1])
    line = f.readline()
f.close()
