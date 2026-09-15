a = lambda x : x[1]

def sort_dictitems(fun, d):
    i =list(d.items())
    for j in range(len(i)):
        for k in range(len(i)-1):
            if fun(i[k])> fun(i[k+1]):
                i[k],i[k+1]=i[k+1], i[k]

    return dict(i)




students = {
    "Aman": 78,
    "Rahul": 56,
    "Sneha": 92,
    "Priya": 88,
    "Arjun": 45,
    "Neha": 67,
    "Kiran": 39,
    "Rohit": 81,
    "Anjali": 74,
    "Vikram": 60
}

print(sort_dictitems(a, students))