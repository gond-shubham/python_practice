a = 3
for i in range(1, 5):
    print(' '*a, end='')
    for j in range(1, i+1):
        print(j, end=' ')
    a= a-1
    print()
b= 1
for x in range(3, 0, -1):
    print(' '*b, end='')
    for y in range(1, x+1):
        print(y, end=' ')
    b=b+1
    print()
