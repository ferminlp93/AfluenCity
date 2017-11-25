import csv

with open('output.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    for row in readCSV:
        print(row)
