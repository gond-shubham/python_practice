# Extract Unique values dictionary values

data = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}
res=[]

for x in data.values():
    for i in x:
        if i not in res:
            res.append(i)
print(res)


        
    
