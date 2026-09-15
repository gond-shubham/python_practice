A=[1,2,3,4,5]
B=[10, 20, 30, 40, 50]

gen_obj = ((i,j) for i in A for j in B)

for i in gen_obj:
    print(i)      # print(next(gen_obj))






