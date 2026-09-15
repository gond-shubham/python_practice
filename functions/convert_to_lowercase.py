def lower(object):
    str1 = ""
    for i in object:
        if "A"<=i<="Z":
            str1 = str1 + chr(ord(i)+32)
        else:
            str1 = str1+i
    return str1

print(lower(input("enter :")))