a=lambda x: x**2

def square_list(fun, l):
    a=[]
    for i in l:
        a.append(fun(i))
    return a

A=[2,4,5,6,8,6,12,34,56,78]

L=square_list(a, A)

print(L)

