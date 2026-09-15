a=lambda x,y:x+y

def add_num(fun, num, list):
    for i in range(len(list)):
        list[i]=fun(list[i], num)
    return list

A=[1,2,3,4,5,6,7,8]

print(add_num(a, 10, A))
