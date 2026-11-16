# creating the dict with the input value a key

N = int (input())
D={}

if N >= 10:
    for i in range(1,10):
        D[i] =[]
else:
    for i in range(1, N+1):
        D[i] =[]
        


for i in range(1, N+1):
    sum1=0
    b=i
    while i>0:
        a=i%10
        sum1 = sum1 +a
        i = i //10
    if sum1 in D:
        D[sum1].append(b)
    else:
        for x in D:
            if sum1 in D[x]:
                D[x].append(b)
    
          
        
v = list(D.values())
print(v)

max1 = 0
c=0
for y in v:
    if len(y)>max1:
        max1 = len(y)
    if max1==len(y):
        c=c+1
print(c)

