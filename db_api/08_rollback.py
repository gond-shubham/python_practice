import sqlite3 as sql

id=int(input("please enter the employee id: "))
salary= float(input("please enter the salary: "))
db_connect=sql.connect("company.db")
cursor_obj=db_connect.cursor()
cursor_obj.execute("update employees set salary=? where emp_id=?",(salary, id))
db_connect.rollback()
cursor_obj.execute("select * from employees where emp_id=?", (id,))
print(cursor_obj.fetchone())

cursor_obj.close()
db_connect.close()
