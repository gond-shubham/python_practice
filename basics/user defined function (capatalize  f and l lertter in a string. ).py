text = input()
char = input()
str1=''
str2=''
List = []
for i in text:
    if i != char:
        str1 =str1 + i
    else:
        for i in range(len(str1)):
            if i == 0 or i == len(str1)-1:
                str2 = str2 + str1[i].upper()
            else:
                str2 = str2 + str1[i].lower()
        List.append(str2)
        str1=''
        str2=''

        
if str1!='':
    for i in range(len(str1)):
            if i == 0 or i == len(str1)-1:
                str2 = str2 + str1[i].upper()
            else:
                str2 = str2 + str1[i].lower()
    List.append(str2)
    str1=''
print(List)
        
str1 =' '.join(List)
print(str1)
