import sqlite3 as sql
db_connect=sql.connect("company.db")
cursor_obj=db_connect.cursor()

while True:
    try:
        print('''
        1. Add Employee
        2. View Employees
        3. Update Salary
        4. Delete Employee
        5. Exit
        ''')

        option= input("please enter in range of (1-5)")

        match option:
            case '1':
                n=int(input("please enter the no of employees to add: "))
                for i in range(n):
                    id= int(input("please enter the id: "))
                    name=input("please enter the name: ")
                    dept= input("please enter the department name: ")
                    salary = float(input("please enter the salary: "))
                    cursor_obj.execute("insert into employees values(?,?,?,?)", (id, name, dept, salary))
                print(f'{n} employees inserted successfully')

            case '2':
                 cursor_obj.execute("select * from employees")
                 print(cursor_obj.fetchall())

            case '3':
                id = input("please enter the employee id: ")
                salary = float(input("please enter the salary to update: "))
                cursor_obj.execute("update employees set salary=? where emp_id = ?", (salary, id))
                print(f'{id} employee salary update successfully')

            case '4':
                id = input("please enter the employee id: ")
                cursor_obj.execute("delete from employees where emp_id = ?", (id,))
                print(f'employee with {id} deleted successfully')

            case '5':
                print("************** Thank you ************************")
                break

            case _:
                print("Please give the proper input in the range of (1-5)")
    except sql.IntegrityError as e:
        print(f'{e}=the employee id: {id} is already exist, ')
        db_connect.rollback()
    except:
        print("Some issue: team is check on it.")
    finally:
        cursor_obj.close()
        db_connect.close()











