import sys
with open("dict.txt") as f:
    for line in f:
        if sys.argv[1] in line:
            print(line)
