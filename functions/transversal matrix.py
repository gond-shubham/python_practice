# Transversal of matrix.
A=[[1,2,3],
   [4,5,6],
   [7,8,9]]
for k in range(3):
    for i in range(3):
        for j in range(3):
            if k == j:
                print(A[i][j], end=' ')
    print()

