def perfect(num):
    for i in range(1, num):
        if num %i == 0:
            sum = sum + i
    if sum == num:
        return "perfect number"
    else:
        return "non-perfect number"


print(perfect(7))