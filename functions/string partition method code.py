# Partition user defined methods.

text = input()
sepr = input()
str1 =''
List =[]
for i in range(len(text)):
    if  text[i] != sepr:
        str1 = str1 + text[i]
        print(str1)
    else:
        List.append(str1)
        List.append(sepr)
        List.append(text[i+1:])
        break
    
print(tuple(List))

        
                    
            
        
