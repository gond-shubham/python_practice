# List of Dictionaries to List of Lists


a = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name':'nithin', 'age':23}]
L =[]
for x in a:
    for y in x.items():
        L.append(list(y))
print(L)


d=  [list(y) for y in x.items()for x in a]
print(f'this is {d}')

       
