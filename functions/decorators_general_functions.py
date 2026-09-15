def general_decorator(fun):
    def wrapper(*args, **kwargs):        # *args become tuple and **kwargs become dict.
        res= fun(*args, **kwargs)      # unpack the tuple and dict.. with '*' for tuple, '**' for dict.
        return res

    return wrapper


@general_decorator
def main_function(a,b,c,/,*,d,e,f,g):
    x=a+b+c
    y=d*e*f*g
    return y//x

x=main_function(11,12,13,d=5,e=10,f=15,g=20)
print(x)



