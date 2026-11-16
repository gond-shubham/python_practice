# factors frequency dictionary

L = [2, 4, 6, 8]
a = max(L)
d={}

for i in range(1, a+1):
    c=0
    for j in L:
        if j%i == 0:
            c=c+1
    d[i]=c
print(d)
    
        
            
    
    
