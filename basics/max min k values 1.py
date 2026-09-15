A = tuple(sorted((23, 58, 85, 39, 474, 34773, 0)))
k=2

bmin = []
bmax =[]

for i in range(len(A)):
    if i <1:
        bmin.append(A[i])
        
    elif len(bmin) < k:
        if A[i]> A[i -1]:
            bmin.append(A[i])
            

            
    if len(bmax)<k:
        bmax .append(A[i])
    else:
        if A[i]>max(bmax):
            bmax.remove(min(bmax))
            bmax.append(A[i])
print(bmin, bmax)
