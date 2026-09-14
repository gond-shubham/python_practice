# find the prime number ===============


num = int(input("enter any number:"))

i = 2
c = 0

while i < num:
    if num % i == 0:
        c = c + 1
    i = i+1
if c == 0 :
    print(f' the given {num} is  a prime number')
else:
    print(f' the given {num} is  not a prime number')
