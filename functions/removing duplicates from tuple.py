# removing duplicates from tuple

A =  list((1, 3, 5, 2, 3, 5, 1, 1, 3))
b=[]
for i in A:
    if i not in b:
        b.append(i)
print(tuple(b))


# removing duplicate lists from tuple


T =list(([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3]))
c = []
for i in T:
    if i not in c:
        c.append(i)
print(c)


# extract digits from Tuple list



