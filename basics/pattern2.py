for i in range(1,6):
    for j in range(1, 6):
        if j <= i:
            print(i, end=' ')
        else:
            print("*", end = ' ')
    print()




#=========================================================
print()

for i in range(5,0,-1):
    for j in range(1, 6):
        if j<= i:
            print(i, end=' ')
    print()


#===================================================

print()

for i in range(5, 0, -1):
    for j in range(1, 6):
        if j <= i:
            print(j, end=' ')
    print()

#======================================================


print()

for i in range(1, 6):
    for j in range(1, 6):
        if j<=i:
            print(j, end=' ')
    print()



#=======================================================

print()
for i in range(1, 6):
    for j  in range(1, 6):
        if j>=i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()
#============================================================


print()

for i in range(1, 6):
    for j in range(5,0,-1):
        if j<=i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()

#===========================================================

print()

for i in range(5, 0, -1):
    for j in range(1, 6):
        if j>=i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()


#=============================================================



print()
c=1
for i in range(1, 6):
    for j in range(1, 6):
        if j <=i:
            print(c, end=' ')
            c+=1
    print()

    print()
