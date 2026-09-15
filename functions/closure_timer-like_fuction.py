def timer(start_time):
    def inner(end_time): # here the end_time should always be greater than start_time.
        execution_time= end_time - start_time
        return execution_time

    return inner

time = timer(100)
print(time(105))
