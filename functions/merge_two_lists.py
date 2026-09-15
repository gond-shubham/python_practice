def merge(l1, l2):
    for i in l2:
        l1.append(i)
    return l1
a=[5, 4, 3, 2, 1]
b=[9, 8, 7, 6, 5, 4, 3]

print(merge(a, b))