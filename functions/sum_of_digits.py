'''def digit(num):
    sum=0
    while num>0:
        sum = sum + num%10
        num = num //10
    return sum'''



def digit(num):
    a=str(num)
    sum=0
    for i in a:
        sum = sum + int(i)
    return sum

print(digit(120))