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
        n = n // 10
        sum = sum + a ** c
    if z == sum:
          print(f'{z} is a armstrong number')
