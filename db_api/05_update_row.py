import sqlite3 as sql


db_connect = sql.connect("company.db")
cursor_obj = db_connect.cursor()

id= input("please enter the employee id: ")
salary=float(input("please enter the salary to update: "))
cursor_obj.execute("update employees set salary=? where emp_id = ?", (salary, id))
db_connect.commit()

cursor_obj.execute("select * from employees where emp_id=?", (id,))
emp=cursor_obj.fetchone()


print(emp)

cursor_obj.close()
db_connect.close()



