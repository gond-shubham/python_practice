# List of tuples with there values and cubes.

List = map(int, input().split())

L1 = []

for i in List:
    b = i **3
    L1.append((i,b))
print(L1)


A = [[(1,2), (2,4)]]


for i in A[0]:
    list(i).append(7)
print(A)
