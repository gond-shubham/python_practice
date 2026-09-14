# product of the digits in a number.

n = int(input("enter any number:"))
N = n
m=1
while n:
    a = n %10
    m = m*a
    n= n//10
if N==0:
    print("the given number is 0")
else:
    print(f'the mutlipaction of digits in a {N} is {m}')

    
