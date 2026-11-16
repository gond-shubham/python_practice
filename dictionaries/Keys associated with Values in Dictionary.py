#Keys associated with Values in Dictionary

A = {'abc': [10, 30], 'bcd': [30, 40, 10]}


set1=set()
for x in A.values():
    set1.update(x)

d ={}
for y in set1:
    L=[]
    for z in A.keys():
        if y in A[z]:
            L.append(z)
    d[y]=L
print(d)


    
