A=[(6, 24, 12), (60, 10, 5), (12, 18, 21)]

k = 5 
B =[]

for i in A:
    c = 0
    for j in i:
        if j %k==0:
            c = c+1
        if c == len(i):
            B.append(i)
print(B)
            
            
    
