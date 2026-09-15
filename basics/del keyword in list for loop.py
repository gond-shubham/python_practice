A= [10,20,30, 10, 10, 10, 20, 50, 60, 70, 80, 10]

i = 0
value = 10
for _ in range(len(A)):
    if value == A[i]:
        del A[i]
        i = i -1
    i = i+1


print(A)



while value in A:
    A.remove(value)



