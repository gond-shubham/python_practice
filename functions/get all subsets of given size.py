s = list({1,2,3,4,5})

k =2
l = len(s)//2

if len(s)%2 == 0:
    n = l
else:
    n = l +1

L=[]
b=0
for i in range(1, n+1):
    if i != l+1:
        a = []
        a = s[b:k]
        L.append(set(a))
        b=k
        k = k+2
    else:
        a = []
        a=s[b:]
        L.append(set(a))

print(L)



    
    
    
    
