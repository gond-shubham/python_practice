def multiplier(n):
    def inner(value):
        return value *n
    return inner


x=multiplier(5)
print(x(10))
print(x(20))

y = multiplier(10)
print(y(1))
print(y(5))