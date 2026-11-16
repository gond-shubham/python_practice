import sqlite3 as sql

try:
   db_connect=sql.connect("company.db")
   cursor_obj=db_connect.cursor()


   cursor_obj.execute("update employees set salary=100000 where emp_id=101")
   cursor_obj.execute("update employees_data set salary=100000 where emp_id=102")
   db_connect.commit()
except sql.OperationalError as a:
    print(a)
    print("Transaction rolled back successfully")
    db_connect.rollback()

finally:
    cursor_obj.close()
    db_connect.close()
    print("DB resources are deallocated")





