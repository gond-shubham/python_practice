def count_function_calls(fun):
    count=0
    def wrapper(*args, **kwargs):
        nonlocal count
        count+=1
        res = fun(*args, **kwargs)
        print(f'the function call count is {count}')
        return res
    return wrapper





@count_function_calls
def function():
    print("counting the function calls")


function()
function()
