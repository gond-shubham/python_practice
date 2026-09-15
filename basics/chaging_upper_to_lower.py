char = input("enter:")

if 'A' <= char <= 'Z':
    a= ord(char)+ 32
    print(chr(a))
elif  'a' <= char <= 'z':
    b= ord(char)-32
    print(chr(b))
