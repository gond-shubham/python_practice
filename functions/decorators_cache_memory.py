def caching_memory(fun):
    dict={}              #it stores in __closure__ memory
    def wrapper(*args, **kwargs):
        if args in dict:
            print("found in cache memory")
            return dict[args]
        res = fun(*args, **kwargs)
        dict[args] = res
        return res
    return wrapper


@caching_memory
def square_root(a):
    return a*a

x=square_root(5)
print(x)
y=square_root(5)
print(y)

print(square_root.__name__)  #wrapper
print(square_root.__closure__)  # cache memory dict stored in __closure__ cells.
