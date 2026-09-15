def generator_function():
    for i in range(1,11):
        yield i               # yield pause the execution after returning the value


x= generator_function()    # iterator object

print(next(x))    #builtins module next method.
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))