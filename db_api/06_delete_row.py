import sqlite3 as sql

id= input("please enter the employee id: ")
db_connect=sql.Connection("company.db")

cursor_obj=db_connect.cursor()


cursor_obj.execute("delete from employees where emp_id = ?", (id,))
db_connect.commit()

cursor_obj.execute("select * from employees where emp_id =?",(id,))
emp=cursor_obj.fetchone()

if emp is None:
    print(f"deleted successfully")


cursor_obj.close()
db_connect.close()




