import random


def password_generator():
    A=('1234567890')
    B=('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    password=''
    while True:
        for i in range(2):
            password=password+A[random.randint(0, 9)]
        for i in range(6):
            password = password + B[random.randint(0, 51)]
        yield password
        password=''


password = password_generator()

for i in password:
    print(i)

print(password.gi_frame) 


