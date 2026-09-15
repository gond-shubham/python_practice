import functools

def decorator_preserving(fun):
    @functools.wraps(fun)        # it will assign the fun metadata to wrapper
    def wrapper(*args, **kwargs):
        print('*'*20)
        res=fun(*args, **kwargs)
        print('*'*20)
        return res
    return wrapper


@decorator_preserving
def main_fun(a,b):
    "it's a main function"
    return a+b


x=main_fun(12, 14)
print(x)
print(main_fun.__name__)   # main_fun
print(main_fun.__doc__)     # attribute stores "it's a main function"




