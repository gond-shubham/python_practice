A = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
k =2
B=[]
for i in A:
    c = 0
    for j in i:
        if len(str(j))==k:
            c= c+1
        if c == len(i):
            B.append(i)
print(B)


