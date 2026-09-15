def sorting(object):
    N=len(object)
    for i in range(N-1):
        for j in range(N-1):
            if object[j] > object[j+1]:
                object[j],object[j + 1] = object[j + 1],object[j]
        N=N-1
    return object

print(sorting([9, 8, 7, 6, 5, 4, 3]))
