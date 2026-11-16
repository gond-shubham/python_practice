d={'name1': 'hello world', 'name2': 'python code', 'name3': 'world peace'}
word = 'world'

res={}
for i in d:
    a = d[i].split()
    if word not in a:
        res[i]=' '.join(a)
print(res)
    
