# find the armstrong number.  ==============

num = int(input("enter any number:"))
dig = num
value = num
p = 0
sum = 0
while num > 0:
    p = p+1
    num = num//10

print(p)
  

while dig>0:
    a = dig%10
    sum = sum + (a ** p)
    dig = dig // 10
print(sum)
if sum == value:
    print (f'the given {value} is a armstrong number')
