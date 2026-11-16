import sqlite3 as sql


db_connect = sql.connect("company.db")
cursor_obj = db_connect.cursor()

id= input("please enter the employee id: ")
cursor_obj.execute("select * from employees where emp_id = ?", (id,))

emp=cursor_obj.fetchone()

print(emp)

cursor_obj.close()
db_connect.close()



