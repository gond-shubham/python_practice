def remove(object):
    a=[]
    for i in object:
        if i not in a:
            a.append(i)
    return a


print(remove([1,2,3,4,5,6,7,4]))