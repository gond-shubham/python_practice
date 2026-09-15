def gen():
    yield 1
    yield 2
    yield 3


a=gen()
print(a, type(a))
b=a()
