"""def authenticate(function):
    users={'nit':'n123',
           'naresh':'x123',
           'ramesh':'r321'}
    def wrapper():
        uname=input('Enter username: ')
        pwd=input('Enter password: ')
        if uname in users and users[uname]==pwd:
            function()
        else:
            print('Invalid username or password')

    return wrapper

@authenticate
def deposit():
    print("deposit")


@authenticate
def withdraw():
    print("withdraw")"""

def smart_division(function):
    def wrapper(n1,n2):
        if n2==0:
            return 0
        else:
             return function(n1,n2)
    return wrapper

n1= int(input())
n2= int(input())

@smart_division
def division(n1,n2):
    return n1/n2

n3 = division(n1,n2)
print(n3)



