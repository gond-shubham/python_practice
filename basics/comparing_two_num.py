import sys

n1= int(sys.argv[1])
n2= int(sys.argv[2])
print(type(n1))
print(f" {n1} is greater than {n2}") if n1>n2 else print(f" {n2} is greater than {n1}") if n2>n1 else print("both are equal")


                                        
