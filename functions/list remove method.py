A= [10,20,30, 10, 10, 10, 20, 50, 60, 70, 80, 10]
value =10
while value in A:
    b=A.index(value)
    del A[b]

print(A)
