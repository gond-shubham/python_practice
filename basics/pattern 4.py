for i in range(1,6):
    for j in range(1, 6):
        if i == j:
            print("*", end=' ')
        else:
            print(' ', end=' ')
    print()


#===================================================



print()

for i in range(1, 6):
    for j in range(5, 0, -1):
        if i == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#========================================================
print()
c=4
for i in range(1, 6):
    for j in range(1, 6): 
        if j-c == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    c-=1
    print()
#==========================================================


print()

for i in range(1,6):
    for j in range(1, 6):
        if i == j or i+j == 6:
            print("*", end=" ")
        else:
            print(' ', end=' ')
    print()



#==============================================================


print()

for i in range(1,6):
    for j in range(1, 6):
        if j == 1 or j ==5 :
            print("*", end=' ')
        else:
            print(' ', end=' ')
    print()

#================================================================


print()

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5:
            print('*', end=' ')
        elif j == 1 or j == 5:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


# ==================================================================


print()

for i in range(1,6):
    for j in range(1,10):
        if i +j == 6 or i + j == 8 or i + j == 12 or i+j ==14:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()


































