def outer():
    c=0
    def counter():
        nonlocal c
        c=c+1
        return c
    return counter

x=outer()
print(x())
print(x())
print(x())