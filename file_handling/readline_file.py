with open('names.txt', 'r') as file:
    c=1
    while True:
        line = file.readlines()
        if line == '':
            break

        print(f'{c}.{line.strip()}')
        c+=1



