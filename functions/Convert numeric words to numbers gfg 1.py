text = input().split()


List = [['one', 1],
        ['two', 2],
        ['three', 3],
        ['four', 4],
        ['five',5],
        ['six', 6],
        ['seven', 7],
        ['eight', 8],
        ['nine', 9],
        ['zero', 0]]

str1= ''

for i in text:
    for j in List:
        if i == j[0]:
            str1 = str1 + str(j[1])
        else:
            if  i not in ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']:
                print('check the word', i)
                break
            
            
        
print(str1)
