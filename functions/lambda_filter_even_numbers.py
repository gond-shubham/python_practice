a=lambda x: True if x%2 ==0 else False

def even(fun, list):
    l=[]
    for i in list:
       if fun(i):
           l.append(i)
    return l

A=[2,4,5,6,7,8,9,12,34,55,67,78,99]
print(even(a, A))