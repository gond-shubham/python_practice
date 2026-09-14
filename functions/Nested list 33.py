# creating nested list 3X3.

A = []
v = 1
for i in range(3):
    A.append([])
    for _ in range(3):
        A[i].append(v)
        print(v)
        v = v + 1
print(A)
        
