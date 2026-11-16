# Inversion in nested dictionary
A = {"a" : {"b" : {}}, "d" : {"e" : {}}, "f" : {"g" : {}}}

#L = list(A.items())
#print(L)

res ={}
for x in A:
    for y,z in A[x].items():
        res.update({y:{x:z}})
print(res)
        
