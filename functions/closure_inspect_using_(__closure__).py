def inspect():
    count= 0
    message= "good morning"
    def inner():
        nonlocal count
        count+=1
        print(f'{message} the count is {count} ')
    return inner

x= inspect()
x()
print(type(x))
print(x.__closure__) # closure is a function attribute..
print(type(x.__closure__)) # it's a type of tuple
print(type(x.__closure__[0])) # the closure stores references to cells
print(x.__closure__[0].cell_contents) # in cells the actual value get stores.
print(x.__closure__[1].cell_contents)

