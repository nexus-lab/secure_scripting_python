f = open("connect.csv", 'r')
count = 0
for line in f:
    tokens = line.split(",")
    toPrint = "first field "+tokens[0]+", last field"+tokens[10]
    print toPrint.strip()
    count = count + 1
print "Read "+str(count)+" lines"
