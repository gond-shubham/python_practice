# print 1 to 10

i =1
while i<=10:
    
    print(i)
    i = i+1

#===========================================================================

print()

i = 10
while i >=1:
    print(i)
    i = i -1

#=========even numbers from 1 to 20 ========================


print()

i = 1
while i <= 20:
    if i %2 ==0:
        print(i)
    i = i+1


#============ sum of first 10 natural number ==========



print()

i = 1
n=0

while i <= 10:
    n= n +i
    i = i+1
print(n)




# ============== Take 5 numbers from the user and print their total  ========

print()
num = 0
i = 1
while i <=5:
    n =int(input("enter the number:"))
    num = num +n
    i = i+1

print(num)



# ==========Count how many digits are in a number  =================

num = int(input("enter the number:"))
n= 0

while num>0:
    num = num // 10
    n = n+1
print(n)


# ====================  Reverse a number  ============



num = int(input("enter the number:"))

Reverse = ""
while num>=10:
    n = num% 10
    d=str(n)
    Reverse = Reverse + d
    num = num//10
    
print(Reverse)




# ============== Find the sum of digits ===================================


digit = int(input("enter the number:"))

sum = 0

if digit < 10:
    print(f'sum of the  number is {digit}')

while digit >=10:
    n = digit % 10
    sum = sum + n
    digit = digit // 10
    if digit < 10:
        sum = sum + digit
print(sum)



# ========================= Check if a number is palindrome =================

number = int(input("enter the number:"))

Reverse= ""

if number <10:
    print("the number is palindrome", number)

































        

    



    
