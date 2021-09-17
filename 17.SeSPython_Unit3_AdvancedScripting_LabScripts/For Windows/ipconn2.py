import time
import datetime
f = open("connect.csv", 'r')
toPrint = ""
COUNT = 0
for line in f:
    tokens = line.split(",")
    now = datetime.datetime.now()
    if COUNT == 0:
        TIMESTAMP = "TIMESTAMP"
    else:
        TIMESTAMP = now.strftime("%a %b %d %H:%M:%S %Z %Y")+tokens[1]+" "+tokens[2]

    toPrint += tokens[0]+","+tokens[1]+","+tokens[2]+","+TIMESTAMP+","+\
              tokens[3]+","+tokens[4]+","+tokens[5]+","+tokens[6]+","+\
              tokens[7]+","+tokens[8]+","+tokens[9]+","+tokens[10]
    COUNT = COUNT + 1
out = open("connect-ts.csv", 'w')
out.write(toPrint)
