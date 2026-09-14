s = ' '
a = 4
for i in range(1, 6):
    print( s*a, end='')
    for j in range(1, i+1):
        if i == j:
            print('1', end=' ')
        else:
            print(j, end=' ')
    a-=1
    print()
    
