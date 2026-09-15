def outer():
    def inner():
        print("It's a inner function")
    return inner


x=outer()
x()