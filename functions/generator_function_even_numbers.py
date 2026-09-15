def generate_evennumbers():
    for i in range(0,100, 2):
        yield i



x=generate_evennumbers()

for i in x:
    print(i)