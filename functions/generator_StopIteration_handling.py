def generator_function():
    count=10
    while count>0:
        yield count
        count-=1


g1=generator_function()
for i in g1:
    print(i)             # for loop iterate until all yield complete.

g2= generator_function()

try:
    for _ in range(15):
        print(next(g2))   # next() -> cannot handle the StopIteration automatically.
except StopIteration:
    print("StopIteration: generator function is exhausted")




