def vowels(a):
    c=0
    for i in a:
        if i in 'aeiouAEIOU':
            c+=1
    return c

print(vowels(input("enter :")))