def exponent(power):
    def inner(value):
        print(value ** power)
    return inner

x=exponent(2)
x(5)
y= exponent(3)
y(5)