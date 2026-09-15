def list_sum(l):
    if len(l)==0:
        return 0

    return l[0]+list_sum(l[1:])


value = list_sum([1,2,3,4,5,6,7,8])
print(value)