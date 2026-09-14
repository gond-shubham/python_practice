

Bal = int(input("enter the balance amount:"))
Amt = int(input("enter the withdrawl amount:"))

if Amt <= 0:
        print("Invalid withdrawal amount")
elif Amt > Bal:
        print("Withdrawal failed: insufficient balance")
elif Bal - Amt < 1000:
    print("Withdrawal denied: minimum balance rule violated")
elif Amt > 10000:
    D = Amt*2/100
    if Bal - (Amt + D)<1000:
        print("Withdrawal denied: minimum balance rule violated")
    else:
        print("Transaction successfull")
        print(Amt)
        print(f'{Bal - (Amt + D)}')
else:
    print("Transaction successful")
    print(Amt)
    print(f' { Bal - Amt}')
