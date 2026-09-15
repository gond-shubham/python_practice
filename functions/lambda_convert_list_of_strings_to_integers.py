a = lambda x: int(x)

def list_int(fun, A):
    for i in range(len(A)):
        A[i]=fun(A[i])
    return A

L =['1', '2', '3', '4', '5', '6', '7', '8']
print(list_int(a, L))