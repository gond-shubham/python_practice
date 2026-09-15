# split function


text = input()
char = input()
maxs = int(input())
List=[]
str1 =''
c = 0

for i in range(len(text)):
    if maxs == c:
        for j in range(i, len(text)):
           str1 = str1+text[j]
        List.append(str1)
        break
    if text[i] != char:
        str1 = str1 + text[i]
    elif str1 != '':
        List.append(str1)
        str1 =''
        c =c+1
    
if str1!= '' and maxs != c:
    List.append(str1)
print(List)
    
        
        
        
    
