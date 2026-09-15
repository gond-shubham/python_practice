a=lambda x: x[1]

def sort_2(fun, t):
    a=list(t)
    for i in range(len(a)):
        for j in range(len(a)-1):
            if fun(a[j])>fun(a[j+1]):
                a[j],a[j+1]=a[j+1], a[j]
    return tuple(a)


data = ("az", "by", "cx", "dw", "ev","fu", "gt", "hs", "ir", "jq")

print(sort_2(a, data))



