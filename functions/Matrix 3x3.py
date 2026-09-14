# creating 3x3 matrix during run time.

M = []

for i in range(3):
    M.append([])
    for j in range(3):
        v = int(input("enter the marks:"))
        M[i].append(v)
print(M)


n = 0
for k in M:
    n = n+1
    t = 0
    c= 0
    for i in k:
        t = t+i
        c +=1
    print(f' the total of {n} is {t} and the average is {t//c}:')
    
