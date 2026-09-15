even= (num for num in range(0,99) if num%2 ==0)

for _ in range(10):
    print(next(even))