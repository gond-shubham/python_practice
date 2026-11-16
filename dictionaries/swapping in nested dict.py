# Swapping Hierarchy in Nested Dictionaries
A = {'Gfg': { 'a' : [1, 3, 7, 8], 'b' : [4, 9], 'c' : [0, 7]}} 
res ={}
for k in A:
    for i in reversed(A[k]):
        res.update({i:{k:A[k][i]}})
print(res)
        
        
