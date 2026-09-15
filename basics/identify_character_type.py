# identifying input character.

char = input("enter any character")

A = ord(char)

if  65 <= A <= 90 or 97 <= A <= 122:
    print("it is a character")
elif 48 <=A <= 9:
    print("digit")
else:
    print("it's a special character")
          
