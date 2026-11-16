#Sort Nested keys by Value
Dict ={'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
        'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
        'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}



'''for x in Dict:
    a=[]
    for y in Dict[x]:
        b=(y, Dict[x][y])
        a.append(b)
    Dict[x]=a'''

Dict1={}

for j in Dict:
    c= list(Dict[j].items())
    for k in range(len(c)-1):
        for i in range(len(c)-1): #01
          if c[i][1]>c[i+1][1]:
            c[i],c[i+1]=c[i+1],c[i]
    Dict1[j]=dict(c)
print(Dict1)

    


        
           
        
    
