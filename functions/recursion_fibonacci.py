def fib(n):
    if n ==0:
        return 0
    elif n==1:
        return 1

    return fib(n-1)+fib(n-2)


value = fib(10)
print(value)

for i in range(11):
    print(fib(i), end = '\t')