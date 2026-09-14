text = input()
str1=''
if len(text) % 2 ==0 and text != '':
    for i in range(len(text)//2):
        str1=str1+text[i]
    str1 = str1*2
    if str1==text:
        print("the given string is symmetric")
    else:
        print("the given string is not symmetric")
else:
    print("the text is not in even number. So' it's not symmetric")


        


