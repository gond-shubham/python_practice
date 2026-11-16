A = [1,2,3,4,5]
B = {'q', 'a', 'v','b','n'}

d = range(5)

m = map(str, A)
s2 ={value for value in d}

for value in m:
    print(value)

s = {value for value in d}
s1 = {value for value in d}

print(s, s1, s2)
