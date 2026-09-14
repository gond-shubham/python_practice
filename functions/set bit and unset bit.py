n= int(input("enter any binary number:"))

c1 = 0
c2 = 0
if n==0:
    c2 = c2+1
while n>0:
    a = n % 10
    if a == 1:
        c1 = c1 +1
    elif a == 0:
        c2 = c2 +1
    n = n // 10

print(f' set bit{c1}')
print(f'unset bit {c2}')





