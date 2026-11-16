#Dictionary with maximum count of pairs
A=[{"gfg": 2, "best" : 4}, {"gfg": 2, "is" : 3, "best" : 4, "CS" : 9}, {"gfg": 2}]

maxi=0
for x in A:
    c=0
    for i in x:
        c=c+1
    if c>maxi:
        maxi=c
        
print(maxi)    
        
#===========================================================================#

keys = ["name", "age", "city"]
values = ["Harry", 30, "New York"]

l=len(keys) if len(keys)<len(values) else len(values)

d={}
for i in range(l):
    d.update({keys[i]:values[i]})
print(d)
