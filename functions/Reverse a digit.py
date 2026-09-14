# Reverse a number  0r palindrome of a number


num = int(input("enter the number:"))
dig = num
Reverse = ""
while num>0:
    n = num% 10
    d=str(n)
    Reverse = Reverse + d
    num = num//10
    
print(Reverse)

if int(Reverse) == dig:
    print("it's a palindrome number")
