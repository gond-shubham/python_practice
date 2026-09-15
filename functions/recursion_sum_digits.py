def digits_count(num):
    if num <=9:
        return num
    return num%10 + digits_count(num//10)

print(digits_count(123))

