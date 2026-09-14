text = input("enter the string: ")
width = int(input("enter: "))
char = input()

str1 =''
#the length of the string must be smaller than width
c = width - len(text)


if c % 2 ==0:
    str1 = (char * (c//2) )+ text +( char * (c//2))
else:
    str1 = (char * ((c//2) + 1)) + text + ( char * (c//2))
print(str1)
