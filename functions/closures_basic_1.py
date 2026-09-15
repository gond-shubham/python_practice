def name(n):
    def inner():
        print(f'my name is {n}')
    return inner

x=name("Gond Shubham")
x()
y=name("kommera nithin reddy")
y()