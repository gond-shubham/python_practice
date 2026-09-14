# string right to left alignment method.

text = input()
width = int(input())
char = input()

str1 =''
c = width - len(text)

for i in range(width -1):
    if i < c:
        str1 = str1 + char
    else:
        str1 = str1 + text
        break
print(str1, len(str1))
    
    
#b=char *( width - len(text)) + text
#print(b)
