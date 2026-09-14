A = [[1,2],
     [2,4]]
B = [[23,56],
     [45,56]]


n = int(input())
m = int(input())
A = []
B = []
for i in range(n):
    A.append([])
    B.append([])
    for j in range(m):
        a = int(input())
        A[i].append(a)
    
    
    

c = []
for i in range(len(A)):
    c.append([])
    for k in range(len(A[i])):
        v = A[i][k] + B[i][k]
        c[i].append(v)
print(c)
        
        
