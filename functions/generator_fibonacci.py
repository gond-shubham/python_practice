def fibonacci():
    first =0
    second = 1
    while True:
        yield first
        x= first
        first = second
        second = x + second



f = fibonacci()

for i in range(100):
    print(next(f))