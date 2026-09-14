#electric bill

unit = int(input("enter the no of unit:"))

if unit <= 100:
    print(" the bill is free")
elif unit <= 200:
    print(f' the bill for the {unit} unit is { unit*5 -500}')
elif unit > 200:
    print(f' the bill for the {unit} unit is { unit*10 -1500}')
    
