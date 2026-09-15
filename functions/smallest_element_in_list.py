def smallest(object):
    mini = object[0]
    for i in object:
        if i<mini:
            mini = i
    return mini

print(smallest([29,34,6,7,99,12,0]))