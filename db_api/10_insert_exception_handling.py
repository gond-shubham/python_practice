import sqlite3 as sql

try:
    db_connect=sql.connect("company.db")
    cursor_obj=db_connect.cursor()
    n=int(input("please enter the no of employees to insert: "))
    for i in range(n):
        id= int(input("please enter the id: "))
        name=input("please enter the name: ")
        dept= input("please enter the department name: ")
        salary = float(input("please enter the salary: "))
        cursor_obj.execute("insert into employees values(?,?,?,?)", (id, name, dept, salary))
    db_connect.commit()
    print(f'{n} employees inserted successfully')

except sql.IntegrityError as e:
    print(f'{e}:{id} is already exist ')
    db_connect.rollback()

finally:
    cursor_obj.close()
    db_connect.close()


