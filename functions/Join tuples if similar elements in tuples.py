A = [(5,6), (5,7),(5,8), (6,10), (7, 13)]


Ie=[]
B=[]
    

for i in range(len(A)):
    if A[i][0] not in Ie:
        B.append(list(A[i])) 
    
    for j in range(len(A)):
        if i !=j:
            if A[i][0] == A[j][0] and A[j][0] not in Ie:
                B[i].append(A[j][1])
                
    Ie.append(A[i][0])
print(B)
        
    
