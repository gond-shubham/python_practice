def square(a):
    return a**2

x=square(5)


def numcheck(a):
    if a %2 == 0:
         print("even")
    else:
         print("odd")

#numcheck(27)


def larger(a,b):
    if a>b:
        return a
    elif b>a:
        return b
    else:
        return f'{a} and {b} are same numbers'

a = larger(5,5)




def fun2(a,b):
    print(a)
    return b


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a, b):
    return a*b

def calculator(a,b):
    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))

#calculator(2,4)


def celsius_to_fahrenheit(c):
     return (9/5*c + 32)

def inpu():
    c = int(input("enter the temperature: "))
    a =celsius_to_fahrenheit(c)
    print(a)

#inpu()

def even(a):
    if a %2 ==0:
        return "even"
    else:
        return "not even"

def positive(a):
    if a>=0:
        return "positive"
    else:
        return "not positive"

def analyze(a):
    print(f' {a} {even(a)}, "and", {positive(a)}')

analyze(5)


