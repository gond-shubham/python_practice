def outer(g):
    def outer(name):
        print(f'{g} {name}')
    return outer


x=outer("good morning")
x("gond shubham")