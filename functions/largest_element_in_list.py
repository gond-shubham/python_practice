def largest(object):
    m = object[0]
    for i in object:
        if i>m:
            m =i
    return m

A=[29,34,6,7,99,12,0]
print(largest(A))