def converter(type):
    def inner(t):
        if type == "Fahrenheit":
            return (t*1.8)+32
        elif type =="Celsius":
            return (t-32)*5/9
    return inner


x=converter("Fahrenheit")
y=converter("Celsius")