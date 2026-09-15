def reverse_string(str):
    for i in range(-1, -(len(str)+1), -1):
        yield str[i]



a="Palindrome"
x=reverse_string(a)

for i in a:
    print(next(x))



