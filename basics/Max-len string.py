#write a program to print the string values in ascending order.

A = ["shubham", 'nithin', 'Anil', 'santhosh', 'laxman', 'harshith']
max = len(A[0])
maxv= A[0]
for v in A:
    if len(v)>=max:
        max= len(v)
        maxv = maxv + " " + v
        

print(f' the maximum length string in {A}is -- {maxv} --{max}')
