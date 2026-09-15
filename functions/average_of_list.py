def suml(list):
    sum=0
    c=0
    for i in list:
        sum=sum+i
        c+=1
    return round(sum/c, 2)


A=[29,34,6,7,99,12,0]
print(suml(A))