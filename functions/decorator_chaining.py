def decorator1(fun):
    def wrapper1(*args, **kwargs):
        print("before----decorator1-wrapper1")
        res =fun(*args, **kwargs)
        print("After----decorator1-wrapper1")
        return res
    return wrapper1

def decorator2(fun):
    def wrapper2(*args, **kwargs):
        print("before----decorator2-wrapper2")
        res = fun(*args, **kwargs)
        print("After----decorator2-wrapper2")
        return res
    return wrapper2

@decorator1
@decorator2                #decorator applies from bottom to top.
def main_fun():
    print(f'the "main_fun" function is decorated with "decorator1" and "decorator2" ')


main_fun()
print(main_fun.__name__)  # main_fun = decorator1(decorator2(fun)) (main_fun = wrapper1)








