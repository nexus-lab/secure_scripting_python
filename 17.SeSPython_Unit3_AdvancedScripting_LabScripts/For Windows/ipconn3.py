from datetime import timedelta, datetime
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

BEGINTIMESTAMP = BEGINTIMESTAMP.partition("98 ")[2]
ENDTIMESTAMP = ENDTIMESTAMP.partition("98 ")[2]

d1 = datetime.strptime(BEGINTIMESTAMP, "%H:%M:%S %p")
d2 = datetime.strptime(ENDTIMESTAMP, "%H:%M:%S %p")

print("Begin: "+BEGINTIMESTAMP+" End: "+ENDTIMESTAMP+" Duration:", (d2-d1))#"+" seconds")#(`expr $DUR / 3600`:`expr $DUR / 60 % 60`:`expr $DUR % 60`)"
exit(0)
