import time
def time_measurement(fun):
    def wrapper(*args, **kwargs):
         start = time.time()
         fun(*args, **kwargs)
         end = time.time()
         return f'the execution time of {fun.__name__} is {end - start}'
    return wrapper


@time_measurement
def work():
    for i in range(1, 11):
        print(i)


print(work())