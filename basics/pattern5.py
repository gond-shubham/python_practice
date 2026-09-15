for i in range(1,6):
    for j in range(1,10):
        if i +j == 6 and j < 6:
            print('*', end='')
        elif i + j == 8 and j<7:
            print('*', end='')
        elif i +j == 10 and j < 8:
            print('*', end='')
        elif i +j ==12 and j<9:
            print('*', end='')
        elif i + j == 14:
            print('*', end='')
        else:
            print(' ', end='')
    print()


