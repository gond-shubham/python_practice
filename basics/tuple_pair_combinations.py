A = (7,2)
B=(7,8)

c=[]
for i in range(2):
    for j in range(2):
        t1 = A[i], B[j]
        t2 = B[j], A[i]
        c.append(t1)
        c.append(t2)
print(c)
