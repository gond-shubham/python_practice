# =============finding largest digit in the number ==============

n =int(input('enter any number:'))
d = n
l = 0
while n:
    a = n % 10
    if a >= l:
        l = a
    n = n//10

print(f'the largest value in {d} is {l}')
    
