def charfreq(object, char):
    c=0
    for i in object:
        if i == char:
            c+=1
    return c

print(charfreq(object = "python is a programming language", char = "p"))


