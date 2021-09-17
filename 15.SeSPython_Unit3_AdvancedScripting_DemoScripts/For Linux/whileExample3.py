f = open("gleep2", 'r')
for line in f:
    tokens = line.split(",")
    toPrint = tokens[0]+" followed by "+tokens[1]
    print(toPrint.strip())
