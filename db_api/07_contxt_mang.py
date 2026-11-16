#context manager automatically deallocates the resources after completion of with block.
#The important DB-API behavior here is that an exception causes the transaction to be rolled back, and the connection is then closed when leaving the with block.
#The context manager automatically handles the connection's transaction context and closes the database connection when the with block ends..

import sqlite3 as sql

id=int(input("please enter the employee id: "))
salary= float(input("please enter the salary: "))
with sql.connect("company.db") as db_connect:
    cursor_obj=db_connect.cursor()
    cursor_obj.execute("update employees set salary=? where emp_id=?",(salary, id))
    cursor_obj.execute("select * from employees where emp_id=?", (id,))
    print(cursor_obj.fetchone())






