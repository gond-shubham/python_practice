import csv

with open("employees.csv", 'w', newline='') as file:
    emp_obj= csv.DictWriter(file,  fieldnames = ('id', 'name', 'age', 'salary'))
    emp_obj.writeheader()

    n=int(input("enter the no of employees: "))

    for _ in range(n):
        id=input("enter the employee id: ")
        name= input("enter the employee name: ")
        age= input("enter the employee age: ")
        salary= input("enter the employee salary: ")

        emp_obj.writerow({'id': id, "name": name, "age": age, 'salary':salary})

    print("Successfully loaded the data in file")





