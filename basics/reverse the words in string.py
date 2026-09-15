# split function
 
 
text = input()
char = input()


str1 =''

c=0
for i in range(len(text)):
    if text[i] != char:
        str1 = str1 + text[i]
        c=c+1
        
    else:
        if c%2 == 0:
            print(str1)
            str1 = ''
            c = 0
        else:
            str1 = ''
            c=0
if c%2 == 0:
    print(str1)




       



