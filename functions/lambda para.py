A= [1,2,3,4,5]
a=lambda : (i for i in A)
i=a()
print(i, type(i))

d=i
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))


