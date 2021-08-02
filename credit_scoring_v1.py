import csv
name = []
age = []
county = []
county = []
marital_status = []
with open('input.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV, None)  # skip the headers
    for row in readCSV:
        name.append(row[0])
        age.append(row[1])

print(name)
print(age)

n = len(name)

#FOR #3 CODE TO PRINT OUT ALL DETAILS PER APPLICANT 
print ('\nName', 'Age', 'Credit Score\n')
for i in range(0, n):
    print (name[i], age[i])


#TODO 
#1. Fill and print the the other 4 lists
#2. Add some more applicants maybe 3 and test it out
#3. For each application, print name, age and credit score on a line
#4. Do some logic like before to decide for applicant [0]
#5. Do the same logic for all applicants using a for loop

print ('\nFin!\n')
