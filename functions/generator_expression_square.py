A=[2,3,4,5,6,7,8,9]

obj1 = (value**2 for value in A)
print(type(obj1))    # generator object

print(next(obj1))
print(next(obj1))
print(next(obj1))