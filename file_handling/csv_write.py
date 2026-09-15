import csv

with open("students.csv", "w", newline='') as students:
    writ_obj=csv.writer(students)
    writ_obj.writerow(('id','name','age','marks'))
    number=int(input("please enter the no of entries: "))
    for i in range(number):
        id=input("please enter the id: ")
        name=input("please enter the name: ")
        age=int(input("please enter the age: "))
        marks= int(input("please enter the marks: "))

        writ_obj.writerow((id, name, age, marks))




