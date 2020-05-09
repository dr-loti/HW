
import csv

with open('ninja.csv') as info:
    reader = csv.DictReader(info)
    for row in reader:
        print((row['Name']), 'is',  (row['Gender']), 'and', (row['Age']), 'years old.')
