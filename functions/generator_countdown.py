def generate_countdown(n):
    while n>=0:
        yield n
        n-=1



c= generate_countdown(10)

for i in range(11):
    print(next(c))