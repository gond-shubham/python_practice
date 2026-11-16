import sqlite3 as sql

db_object=sql.connect("company.db")

cursor_obj=db_object.cursor()

cursor_obj.execute("CREATE TABLE employees(emp_id INTEGER PRIMARY KEY,name TEXT,department TEXT, salary REAL)")
db_object.commit()
cursor_obj.close()


db_object.close()
