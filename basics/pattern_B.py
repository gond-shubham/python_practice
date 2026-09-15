n = int(input())

s = (n*2) - 2
a = 1
b=0
for i in range(1, n*2):
    print(' '*s, end='')
    for j in range(96 + n,96+n-a,-1):
        print(chr(j), end=' ')
    for k in range(n+96+1-b , n+96 +1):
        print(chr(k), end=' ')
    
        
    
    
    s = s-2
    a = a +1
    b = b+1
    print()
  
