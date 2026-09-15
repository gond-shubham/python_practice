def armstrong(num):
    a=num
    sum=0
    while num>0:
        sum = sum + (num%10) ** 3
        num = num //10
    if sum == a:
        return "armstrong"
    else:
        return "non-armstrong"

print(armstrong(153))
