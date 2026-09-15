def power(n):
    def inner(value):
        return value ** n
    return inner

x=power(10)
print(x(2))

y=power(9)
print(y(9))


