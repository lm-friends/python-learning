import csv

name = []
age = []
marital = []
emp_months = []
credit_score = []
#


with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        name = row[0]
        age = row[1]
        #marital status...
        #......
        ......

        name.append(date)
        age.append(color)

    print(dates)
    print(colors)