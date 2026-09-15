gen_obj= (i%2==0 for i in [3,5,7,8,9,10])

print(any(gen_obj))    # True
print(next(gen_obj))    #False
print(next(gen_obj))    #True