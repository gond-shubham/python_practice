# convert nested dictionary to mapped tuple

d = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4}, 'best': {'x': 8, 'y': 3}}

strx=''
stry=''

for key in d:
    a=d[key]
    strx=strx+str(a['x'])
    stry=stry+str(a['y'])

result= [('x', tuple(map(int, strx))), ('y', tuple(map(int, stry)))]
print(result)
