def infinite_square():
    n=0
    while True:
        yield n**2
        n=n+1


s = infinite_square()

for i in range(100):
    print(next(s))