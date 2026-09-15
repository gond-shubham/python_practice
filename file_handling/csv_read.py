import csv

with open("students.csv", "r") as students:
    read_obj=csv.reader(students)

    next(read_obj)

    total_students=0
    highest_mark=0
    lowest_mark=None
    total_marks=0


    for row in read_obj:
        total_students+=1

        id, name, age, marks=row
        total_marks+=int(marks)

        if int(marks)>highest_mark:
            highest_mark=int(marks)

        if lowest_mark is None or int(marks)<lowest_mark:
            lowest_mark=int(marks)

    print(f'Total students: {total_students}')
    print(f'Average marks: {total_marks/total_students}')
    print(f'Highest marks: {highest_mark}')
    print(f'Lowest marks: {lowest_mark}')



