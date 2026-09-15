def log_checking(fun):
    def wrapper():
        print("*" * 15)
        print(f'Executing function: {fun.__name__}')
        print("*" * 15)
        result =fun()
        return result
    return wrapper


@log_checking
def fun1():
    print("Welcome to decorators")


print(fun1())