def custom_range(stop, start =0, step =1):
    if step >0:
        while start<stop:
            yield start
            start +=step
    elif step < 0:
        while stop<start:
            yield start
            start = start +step



r= custom_range(start =0, stop =-5, step =-1)

for i in r:
    print(i, end=' ')