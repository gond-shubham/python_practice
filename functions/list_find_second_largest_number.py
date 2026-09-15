def second(list):
    list.sort(reverse=True)
    for i in range(1, len(list)):
        if list[i]<list[0]:
            s = list[i]
            break
        else:
            return "no second largest value"
    return s

print(second([1, 2, 3, 4, 5, 6, 7]))


