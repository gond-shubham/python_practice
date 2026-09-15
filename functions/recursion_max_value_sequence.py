def max_value(l):
    if len(l)==0:
        return None
    if len(l) ==1:
        return l[0]
    if l[0]<= l[-1]:
        return max_value(l[1:])
    return max_value(l[0:-1])


maxi = max_value([1,2,3,4,5,6,7,8,9])
print(maxi)
