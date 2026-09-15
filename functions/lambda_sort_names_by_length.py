a=lambda x: len(x)

def sort_l(fun, t):
    b=list(t)
    for i in range(len(b)):
        for j in range(len(b)-1):
            if fun(b[j])>fun(b[j+1]):
                b[j],b[j+1]=b[j+1], b[j]
    return tuple(b)


data = (
    "abcdefghij",   # length 10
    "abcdefghi",    # length 9
    "abcdefgh",     # length 8
    "abcdefg",      # length 7
    "abcdef",       # length 6
    "abcde",        # length 5
    "abcd",         # length 4
    "abc",          # length 3
    "ab",           # length 2
    "a"             # length 1
)

print(sort_l(a, data))
