#convert key-value dictionary to list of list.



a= {'name': 'Alice', 'age': 25, 'city': 'New York'}
LoL = [[x,y] for x, y in a.items()]
print (LoL)

