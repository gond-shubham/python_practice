def memory():
    count=0
    def inner():
        nonlocal count
        count+=1
        print(count)
    return inner


x=memory()
x()
x()
x()

y = memory()  # for every closure function there is a different memory space to store count.
y()

print(x,y)  # x, y are different function objects.