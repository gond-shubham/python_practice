def tablegenerator(num):
    for i in range(1, 11):
        for j in range(1, num+1):
            print(f'{j} x {i} = {i*j}', end="\t\t\t\t\t\t\t")
        print()


tablegenerator(10)