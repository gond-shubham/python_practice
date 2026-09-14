A = sorted((23, 58, 85, 39, 474, 34773, 0))
k=2

bmin = []
bmax =[]


for i in range(len(A)):
    if i <1:
        bmin.append(A[i])
        c = c+1
        
    elif c < k:
        if A[i]> A[i -1]:
            bmin.append(A[i])
            c += 1
    

d = 0
for j in range(-1, -(len(A)+1), -1):
    if j == -1:
        bmax.append(A[j])
        d = d+1

    elif d < k:
        if A[j]<A[j+1]:
            bmax.append(A[j])
            d = d+1


print(bmin, bmax)

#================================================   ******* ===============================================================#


    
        
     
        
        
    
        

            

    

    
        
            



            
    
    
        
            
    
    
