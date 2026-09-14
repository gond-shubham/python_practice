print()
c=1
for i in range(1, 6):
    for j in range(i):
        if j <=i:
            print(c, end=' ')
        c+=1
    print()
