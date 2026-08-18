# Finding factorial of a number ==================

num = int(input("enter any number:"))
dig = num
i = 1
while dig > 0:
    i = i * dig
    dig = dig -1


print(f' the factorial of the given {num} is {i}')
