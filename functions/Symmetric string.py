# to check the string is symmetric or not
A= input("enter the word")

j = len(A)//2
flag=True

for i in range(len(A)//2):
   if len(A)%2 ==0:
     if A[i]!=A[j]:
         flag=False
         break
   else:
     flag = False
     break
   j=j+1
    
   

if flag and len(A)!=1:
    print("it's symmetric")
else:
    print("it's not symmetric")
     
    
        
        
        
    
