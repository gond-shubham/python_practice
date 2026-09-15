def fibonacci(num, c=2, A=(0,1)):
    if num == 0:
        return A
    elif num ==1:
        return 1
    else:

        if num == c:
            return A
        A.append(A[-1]+A[-2])
        c+=1
        return fibonacci(num, c, A)


print(fibonacci(15))
print(fibonacci(14))

                              


