#Traingle inequality rule

n1 = float(input("enter the first side of triangle:"))
n2 = float(input("enter the second side of triangle:"))
n3 = float(input("enter the third side of triangle:"))


print("it's a triangle") if n1+n2>n3 and n2+n3>n1 and  n1+n3>n2 else print("it's not a triangle")
