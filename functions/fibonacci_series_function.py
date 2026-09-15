def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    else:
        a=[0,1]
        for i in range(2, num):
            a.append(a[-1]+a[-2])
        return a


print(fibonacci(int(input("enter:"))))