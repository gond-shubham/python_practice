#scoring matrix

D = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}
L= [['gfg', 'best'], ['geeks'], ['is', 'for']]
L1=[]
for x in L:
    s=0
    for y in x:
        s= s+D[y]
    L1.append(s)
print(L1)

