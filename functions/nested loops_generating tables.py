# 1 to 10 tables from for loop ==============

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} X {j} = {i*j}')
    print()

print("===============================================" *2)


i = 1
while i <=10:
    j = 1
    while j <= 10:
        print(f'{i} X {j} = {i*j}')
        j+=1
    i+=1
    print()
