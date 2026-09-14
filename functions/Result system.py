def total_marks(sub=5):
    x = input("enter the marks").split()
    total = sum(list(map(int, x)))
    global z
    z = total
    return total


def average_marks(sub=5):
    average= x/sub
    return average

def percent(sub =5):
    y = x/(sub*100)* 100
    return y



def students_result():
    print("the total marks is", x)
    print("the average marks is", average_marks())
    print("the CGPA grade", percent())

#students_result()
total_marks()
print(z)