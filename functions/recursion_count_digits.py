def digits_count(num):
    if num <=9:
        return 1
    return 1 + digits_count(num//10)

print(digits_count(123))

