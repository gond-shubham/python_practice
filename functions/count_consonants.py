def constants(a):
    c=0
    for i in a:
        if i not in "aeiouAEIOU":
            c+=1
    return c

print(constants(input("enter :")))


