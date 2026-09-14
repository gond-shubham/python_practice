# Smallest and the largest digit in a given value ====

num = int(input("enter any number:"))
N = num
b = num % 10
l = 0

while num>0:
    a = num %10
    if a >= l:
        l = a
    if a <= b:   # only if we have to use not elif:
        b =a
    num = num // 10
if N == 0:
    print(f' the largest and smallest value in the {N} is 0')
else:
    print(f' the smallest value is {b} and largest is {l}')
        
