test = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6, 'KNR':7}
original =test.copy()

k =3
L = []
while len(test)!= 0:
    res ={}
    c=0
    for i in test:
        res[i] = test[i]
        c= c+1
        if c ==k:
            break
    L.append(res)
    for j in res:
        del test[j]
    

print(L)
test = original

        
        
    
