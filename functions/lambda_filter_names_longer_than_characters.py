a=lambda x: True if len(x) >5 else False

def length(fun, list):
    l=[]
    for i in list:
       if fun(i):
           l.append(i)
    return l

A=["aman", "nithin", "shubham", "bava","riya", "santhosh"]
print(even(a, A))