def upper(object):
    str1=''
    for i in object:
        if "a"<=i<="z":
            str1 = str1 + chr(ord(i)-32)
        else:
            str1=str1+i
    return str1

print(upper(input("enter :")))