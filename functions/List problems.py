A=[2,6, 9, 2,3, 65, 12,34, 98, 35, 23, 12, 87, 44,22, 57]

e = 0
d = 0

for i in A:
    if i % 2 ==0:
        e=e+1
    else:
        d = d+1
print(f'the count of even is {e}')
print(f'the count of odd is {d}')







