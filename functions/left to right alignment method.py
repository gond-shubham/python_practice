# string alignment or justify methods code. (left to right Alignment)

text =input()
width =int(input())
char = input()
str1=''
for i in range(width):
    if i < len(text):
        str1 = str1 + text[i]
    else:
        str1 = str1 + char


print(str1)
    


