A = [   [('hi', 'bye')], [('Geeks', 'forGeeks')],
         [('a', 'b')],    [('hi', 'bye')],
          [('a', 'b')]    ]
B=[]
c= 0
for i in A:
    for k in range(len(A)):
            if c != k:
                if i[0] == A[k][0]:
                    if i[0] not in B:
                        B.append(i[0])
                    
    c= c+1

print(B)
