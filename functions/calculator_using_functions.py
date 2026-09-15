def add(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b


def calculator(x,y, type="add"):
    match type:
        case "add":
            print(add(x,y))
        case "substraction":
            print(substraction(x,y))
        case "multiplication":
            print(multiplication(x,y))
        case _ :
            print("invalid type")

calculator(4,5, type="multiplication")
calculator(4,5, type="addd")  # invalid type

