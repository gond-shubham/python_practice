def generator():
        x= yield
        print(x)




a=generator()
next(a)

try:
    a.send(4)
except StopIteration:
    print("StopIteration: the generator function is exhausted")
