# Write a program to count how many times digit n appears in a number.

num = int(input("enter any number:"))
N = num
n = int(input("enter the value to find:"))

c = 0
while num>0:
    a = num % 10
    if a == n:
        c += 1
    num = num//10

if N == 0:
    print(f'the given number {N} is zero')
else:
    print(f' the count of {n} in a given value is {c}')
