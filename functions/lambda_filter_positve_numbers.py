a=lambda x: True if x>=0 else False

def positive(fun, list):
    l=[]
    for i in list:
       if fun(i):
           l.append(i)
    return l

A=[-10, 25, -7, 0, 18, -45, 67, -2, 99, -100, 34]
print(even(a, A))