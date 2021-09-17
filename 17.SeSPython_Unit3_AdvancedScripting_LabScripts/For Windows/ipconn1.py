f = open("connect.csv", 'r')
for line in f:
    tokens = line.split(",")
    toPrint = tokens[1]+"\t"+tokens[2]
    print(toPrint.strip())
