# bubble sort algorithm

A=[84, 848, 8487, 873, 28, 83, 99, 3039, 0, 884]
N = len(A)
for j in range(1, len(A)+1):
    for i in range(N-j): #9
        if A[i]>A[i+1]:
            temp = A[i]
            A[i] = A[i +1]
            A[i+1] = temp
    #N=N-1  # after completion of inner loop the N value changes

print(A)
