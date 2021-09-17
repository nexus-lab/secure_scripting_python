import csv
with open('connect2.csv') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(" ".join(row))
