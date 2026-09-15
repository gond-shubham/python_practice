def flow():
    print("before yield 1")
    yield 1
    print("before yield 2")
    yield 2
    print("before yield 3")
    yield 3
    print("before yield 4")
    yield 4


f = flow()
print(next(f))
print(next(f))
print(next(f))
print(next(f))