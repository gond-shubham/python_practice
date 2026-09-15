# write a armstrong table form 100 to 999.


for i in range(100, 1000):
    n = i
    sum = 0
    for _ in range(1, 4):
        a = i % 10
        i = i // 10
        sum = sum + a ** 3
    if n == sum:
          print(f'{n} is a armstrong number')

#==========================================================================

v = int(input('enter any number'))


for i in range(1, v):
    n = i
    z = i
    sum = 0
    c = 0
    while i:
       c+=1
       i = i//10
    for _ in range(1, c+1):
        a = n % 10
        i = n // 10
        sum = sum + a ** c
    if n == sum:
          print(f'{z} is a armstrong number')
