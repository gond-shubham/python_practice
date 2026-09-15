# practicing decorator without @decorator.

def decorator(fun):
    def wrapper():
        print("*" * 10)
        fun()      # here the closure memory remembers the main function {fun1}
        print("$" * 10)
    return wrapper

def fun1():
    print("Welcome to python")


fun1 = decorator(fun1)    # Now, fun1 holds wrapper function reference.

fun1()