#pattern 1 ===================================

for i in range(1,5):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


# pattern 2 =====================================

print()
s = 5
for i in range(1, 5):
    for j in range(1, s):
        print(j, end=' ')
    s-=1
    print()

# pattern 3 =======================================


print()
s = 3
for i in range(1, 5):
    print(" "*s, end ='')
    for j in range(1, i+1):
        print(j, end=' ')
    s-=1
    print()

# pattern 4=============================================

print()
s = 1
for i in range(1, 5):
    for j in range(s, 0, -1):
        print(j, end=' ')
    s = s+1
    print()
    
        
#pattern 5 ===============================================
a = 3
b = 0
for i in range(1, 5):
    print(' '*a, end='')
    for j in range(1, i+1):
        print(j, end=' ')
    for k in range(b, 0, -1):
        print(k, end=' ')
    a = a-1
    b= b+1
    print()


# patttern 6 ===========================================
    
         
























