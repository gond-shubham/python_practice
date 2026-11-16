import sqlite3 as sql


db_connect = sql.connect("company.db")

cursor_obj = db_connect.cursor()

#Reading rows from database using cursor object.

cursor_obj.execute("select * from employees")

r=cursor_obj.fetchone()  # it will fetch only one row

r2=cursor_obj.fetchmany(3) # it will fetch 3 rows

rows=cursor_obj.fetchall()  # it will fetch all rows


print(r)
print(type(r[0]))
print("*********************")
for r in r2:
    print(r)

print("****************************")
for row in rows:
    print(row)

cursor_obj.close()
db_connect.close()


