N= int(input())
s= set(map(int, input().split()))
c = int(input())
print(s)

for  i in range(c):
    a = input().split()
    if a[0] == 'pop':
        b=s.pop()
        print(b)
    elif a[0]== 'remove' and int(a[1]) in s:
        s.remove(int(a[1]))
    elif a[0] == 'discard'and int(a[1]) in s:
        s.discard(int(a[1]))
    
        
        
print(s)
