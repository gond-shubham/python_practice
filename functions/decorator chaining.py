def draw_stars(function):
    def wrapper():
        print("*"*50)
        function()
        print("*"*50)
    print(1)
    return wrapper


def draw_dollars(function):
    def wrapper():
        print("$"*50)
        function()
        print("$"*50)
    print(2)
    return wrapper





@draw_stars
@draw_dollars
def display():
    print("PYTHON PROGRAMMING LANGUAGE")