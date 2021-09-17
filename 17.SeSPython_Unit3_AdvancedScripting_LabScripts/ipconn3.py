import time
import datetime
f = open("connect-ts.csv", 'r')
COUNT = 0
BEGINTIMESTAMP = 0
ENDTIMESTAMP = 0
for line in f:
    if COUNT == 1:
        tokens = line.split(",")
        BEGINTIMESTAMP = tokens[3]
    else:
        tokens = line.split(",")
        ENDTIMESTAMP = tokens[3]
    COUNT = COUNT + 1
DUR = ENDTIMESTAMP - BEGINTIMESTAMP

print "Begin: "+BEGINTIMESTAMP+" End: "+ENDTIMESTAMP+" Duration: "+DUR #+" seconds (`expr $DUR / 3600`:`expr $DUR / 60 % 60`:`expr $DUR % 60`)"
exit(0)
