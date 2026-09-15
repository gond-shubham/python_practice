a=lambda x: True if x[0] in "AEIOUaeiou" else False

def vowels(fun, list):
    l=[]
    for i in list:
       if fun(i):
           l.append(i)
    return l

A=["apple", "banana", "orange", "grape", "umbrella",
    "cat", "elephant", "iguana", "tiger", "owl",
    "ant", "monkey", "eagle", "lion", "octopus"]
print(even(a, A))