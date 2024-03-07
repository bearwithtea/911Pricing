import csv

# Path: main.py

file = open('Cars and Bids - Pricing.csv', 'r')
type(file)

csvreader = csv.reader(file)

header = []
header = next(csvreader)
header

rows = []

for row in csvreader: 
    rows.append(row)
    rows

print (rows)

file.close()