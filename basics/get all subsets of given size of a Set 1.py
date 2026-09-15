s= list({1,2,3,4})

k =2

l=0
l1 = 1

L=[]
for i in range(len(s)-1):
    a= {s[l], s[l1]}
    L.append(a)
    l = l+1
    l1 = l1 + 1

print(L)

