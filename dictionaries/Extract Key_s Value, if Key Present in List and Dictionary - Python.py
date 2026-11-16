a = ["Gfg", "is", "Good", "for", "Geeks"]
d = {"Gfg": 5, "Best": 6}
K = "KNR"

if K in a:
    if K in d:
        print(d[K])
    else:
        print(f'{K} is not in {d}')
else:
    print(f'{K} is not in {a}')

