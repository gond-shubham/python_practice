def common(l1,l2):
    l=[]
    for i in l1:
        if i in l2 and i not in l:
            l.append(i)
    return l

a = [9, 8, 7, 6, 5, 4, 3]
b = [5, 4, 3, 2, 1]
print(common(a, b))