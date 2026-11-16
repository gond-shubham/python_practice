#Remove keys with Values Greater than K ( Including mixed values )

d = {'a': 1, 'b': 5, 'c': 'hello', 'd': [1, 2, 3]}
d1= d.copy()
k=3
for x in d:
    a=d[x]
    if isinstance(a, (int, float)) and a > k:
        del d1[x]
print(d1)



# with comprehension.

res={x:y for x,y in d.items() if not(isinstance(y, (int,float)) and y>3)}
print(res)
    
