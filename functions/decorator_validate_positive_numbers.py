def validate_positive(fun):
    def wrapper(*args, **kwargs):
        negative1 = 0
        negative2 = 0
        for i in args:    #checks positional arguments
            if i < 0:
                negative1 +=1
        for i in kwargs:          #checks keyword arguments
            if kwargs[i] < 0:
                negative2 +=1

        if negative1 == 0 and negative2 ==0:
            x=fun(*args, **kwargs)
            return x
        else:
            return "the function contain negative value."
    return wrapper



@validate_positive
def main_function(a,/,*,b):
    return a+b


x=main_function(5, b=-6)
print(x)






