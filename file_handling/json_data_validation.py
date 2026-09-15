import json
try:
    with open("students.json", 'r') as students:
          stu_data = json.load(students)
except FileNotFoundError as f:
    print(f)
    exit()
except json.JSONDecodeError as j:
    print(j)
    exit()
except OSError as o:
    print(o)
    exit()


stu_ids = []

for student in stu_data:
    c=True
    try:
        if student['id'] not in stu_ids:
            stu_ids.append(student['id'])
        else:
            print(f'invalid student: {student["name"]}  --  duplicate ID')
            c=False

        if student['age'] <=0:
            print(f'invalid student: {student["name"]}  --  invalid age')
            c=False

        if  not 0 <= student["marks"] <= 100:
            print(f'invalid student: {student["name"]}  --  invalid marks')
            c=False

        if c:
            print(f'Valid student: {student["name"]}')

    except KeyError as k:
        print(f'{k} error for {student["name"]}')






