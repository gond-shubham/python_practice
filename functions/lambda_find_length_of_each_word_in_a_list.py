a=lambda x:len(x)

def fun(fun, l):
    A=[]
    for i in l:
        A.append(fun(i))
    return A

L=["Nisha", "Deepak", "Rithika", "Manoj", "Aditi"]

print(fun(a,L))