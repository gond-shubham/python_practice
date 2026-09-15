with open("test1.txt", 'r') as file:
    sente=0
    words=0
    char=0
    while True:
        line=file.readline()
        if line=='':
            break
        sente+=1
        words += len(line.split())
        char+=len(line.rstrip('\n'))


print(sente)
print(words)
print(char)

