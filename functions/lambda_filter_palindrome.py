a=lambda x: True if x == x[-1::-1] else False

def palindrome(fun, list):
    l=[]
    for i in list:
       if fun(i):
           l.append(i)
    return l

A=[ "madam", "python", "level", "radar", "apple",
    "civic", "banana", "rotor", "hello", "racecar",
    "world", "refer", "noon", "code", "stats"]
print(even(a, A))