def power(base, exponent):
    if exponent==0:
      return 1
    return base * power(base, exponent-1)


value = power(5,5)

print(value)