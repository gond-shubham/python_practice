
A = [(None, 2), (None, None), (3, 4), (12, 3), (None, )] 

i=0
l= len(A)

while i< l:
    c=0
    for j in range(len(A[i])):
        if A[i][j] != None:
            c = c+1
    if c==0:
        del A[i]
        l=l-1
        continue
    i = i+1
print(A)
            
    

        
        
    
