# pattern problem -1 ================================


for i in range (1, 6):
    for j in range(1, 6):
        if i % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end= ' ')

    print()

print("=======" * 3)



for i in range (1, 6):
    for j in range(1, 6):
        print(1, end = ' ') if j %2 != 0 else print(0, end= ' ')

    print()


