A = [10, 20, 30, 40, 10, 10, 10, 50, 80, 10]
value = 10
i=0
l=len(A)

while True:
    if A[i] == value:
        del A[i]
        
        l = l - 1
        
        if i>=l:
            break
        
        continue
    i = i + 1

print(A)
