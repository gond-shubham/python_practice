students = {

    "Aman": (78, 82, 91, 67, 85),

    "Rahul": (56, 61, 72, 48, 59),

    "Sneha": (92, 95, 90, 94, 98),

    "Kiran": (35, 40, 38, 42, 37),

    "Priya": (88, 76, 84, 79, 91),

    "Arjun": (25, 30, 28, 32, 20),

    "Neha": (65, 70, 68, 72, 66)
}




def total_marks(name):
    total = 0
    a=students[name]
    for i in a:
        total += i
    return total

def average(name):
    a=total_marks(name)
    return a/5


def grade(name):
    avg = average(name)
    if avg >= 90:
        return "A"

    elif avg >= 75:
        return "B"

    elif avg >= 50:
        return "C"

    else:
        return "Fail"

def student_report(name):
    print(f'Name : {name}')
    print(f'Marks : {students[name]}')
    print(f'Total: {total_marks(name)}')
    print(f'Average: {average(name)}')
    print(f'Grade: {grade(name)}')



def student_grade_system(name, type="total_marks"):
    if name in students:
         match type:
            case 'total_marks':
                print(total_marks(name))

            case 'average':
                print(average(name))

            case 'grade':
                print(grade(name))

            case 'student_report':
                student_report(name)

            case _:
                print("please enter the valid type")
    else:
         print("enter the valid type")

def options():
    print("chosse for the below options")
    print("1.total_marks")
    print("2.average")
    print("3.grade")
    print("4.student_report")
    print("5.view")
    print("Note: please type the options in case-sensitive")
    name=input("enter the name of the student:")
    type=input("enter from the above options: ")


    student_grade_system(name, type)



options()

