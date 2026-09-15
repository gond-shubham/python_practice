a=lambda x:x.upper()

def upper(fun, l):
    a=[]
    for i in l:
        a.append(fun(i))
    return a
A=["Aman", "Rahul", "Sneha", "Priya", "Arjun"]

L=upper(a, A)
print(L)