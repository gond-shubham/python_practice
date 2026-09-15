import csv

with open("employees.csv", 'r') as file:
    emp_obj = csv.DictReader(file)

    for emp in emp_obj:
        print(emp)