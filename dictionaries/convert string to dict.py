#convert string in to dictionary

s ="{'a':1, 'b':2, 'c':3}"
key =[]
values=[]
for i in s:
    if 'a'<= i <='z' or 'A'<=i<='Z':
        key.append(i)
    elif '0'<=i<='9':
        values.append(i)

res = dict(zip(key, map(int, values)))
print(res)

        
        
        
