import sys

A=[]
for i  in range(100):
    A.append(i)            # A list contains 0 to 99 values.


def generate_value():  # the generator function generates infinite values.
    first=0
    second =1
    while True:
        yield first
        first = second
        second+=1



value = generate_value()   #value is a generator object.
print(next(value))

print(sys.getsizeof(A))       #list size is 920
print(sys.getsizeof(value))     #generator object size is 192

#generator object stores

print(value.gi_frame.f_locals)  #current value(s)
print(value.gi_frame.f_lineno)   #execution position
print(value.gi_code)






