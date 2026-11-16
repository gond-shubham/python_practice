import sqlite3 as sql

db_object= sql.connect("company.db")
cursor_obj=db_object.cursor()

n=int(input("please enter no of inputs: "))

for i in range(n):
    id=input("please enter the id: ")
    name= input("please enter the name: ")
    Dept= input('please enter the department name: ')
    salary= float(input("please enter the salary: "))

    cursor_obj.execute("insert into employees values(?, ?, ?, ?)",(id, name, Dept, salary))



db_object.commit()
cursor_obj.close()
db_object.close()
