def product(l):
    if len(l)==0:
        return 1
    if len(l) == 1:
        return l[0]
    return l[0]*product(l[1:])

a=product([1,2,4,5,6,7,8,4,56])
print(a)