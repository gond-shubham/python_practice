def words(object):
    str1=''
    c=0
    for i in object:
        if i != ' ':
            str1 = str1 + i
        else:
            if str1 != '':
                c+=1
                str1=""
    if str1 != '':
        c+=1
    return c

print(words(input("enter:")))

