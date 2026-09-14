def outer(f):
    def inner():
        f()
        print(10)
    return inner

@outer
def fun1():
   print("Kommera Nithin Reddy")



x=outer(fun1)
x()



'''def outer():
    def inner():
        print("*"*10)
    return inner

x=outer()'''
















