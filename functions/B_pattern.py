n = int(input())

s = (n*2) - 2
a = 1
for i in range(1, n*2):
    print(' '*s, end='')
    for j in range(96 + n, 96+n-a,  -1):
        print(chr(j), end=' ')
    
    s = s-2
    print()
