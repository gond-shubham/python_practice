def natural_numbers(n):
    if n ==1:
        return 1
    return n + natural_numbers(n-1)


value= natural_numbers(10)
print(value)
