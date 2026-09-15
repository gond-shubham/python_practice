def removespace(a):
    str1=''
    for i in a:
        if i != ' ':
            str1 = str1 +i
    return str1

print(removespace(input("enter:")))