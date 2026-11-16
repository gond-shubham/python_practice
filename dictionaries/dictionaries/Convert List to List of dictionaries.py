# convert list to lists of dictionaries.

a = ["name", "age", "city"]
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]]

d =[]
for i in range(len(a)):
    d.append({ x:y  for x,y in zip(a, b[i])})
print(d)

# list of lists to dictionary

a = [["a", 1], ["b", 2], ["c", 3]]
d ={} 
for x,y in a:
    d[x]=y
print(d)
