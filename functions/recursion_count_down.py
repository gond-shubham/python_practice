def countdown(n):
    if n == 1:
        return print(1)

    print(n)
    countdown(n-1)

countdown(10)