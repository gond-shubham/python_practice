Y = int(input("enter any year:"))

print(f" its a leap year because it is divisble by 4 and not 100") if Y%4==0 and Y%100 != 0 else print("it's a leap year divisible by 400") if Y%400 == 0 else print ("it's  not a leap year")
