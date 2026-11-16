# Nested Dictionary using given List and dict
a = {'Gfg': 4, 'is': 5, 'best': 9}
b = [8, 3, 2]

res={}

c= 0
for key in a:
    res.update({b[c]:{key:a[key]}})
    c = c+1
print(res)
        
