def fun_with_para(count):
    def decorator_function(fun):
        def wrapper(*args, **kwargs):
            print("*************************")
            for i in range(count):
                x=fun(*args, **kwargs)
                print(x)
            print(f'the function executed {count} times')
            return x
        print(decorator_function.__closure__)
        return wrapper
    return decorator_function



@fun_with_para(5)
def fun1(a, b):
    return a+b

x=fun1(5,6)
print(x)
print(fun1.__closure__[0])  # closure memory for the wrapper



