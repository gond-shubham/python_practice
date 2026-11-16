d = {'watermelon': 1, 'apple': 2, 'banana': 3, 'pineapple': 4}

a = list(d.items())

print(a)

for i in range(len(a)-1):
    if len(a[i][0])>len(a[i+1][0]):
        c = a[i]
        a[i]=a[i+1]
        a[i+1]=c

print(a)


f ={}
for i in a:
    x,y = i
    f[x]=y

    
print(f)

    
    
    
    
