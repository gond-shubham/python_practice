def bank():
    balance = 50000
    def inner():
        action= input("enter withdraw/deposit: ")
        amount= int(input("enter the amount: "))
        nonlocal balance
        if action == "deposit":
            balance += amount
            print(f'current balance {balance}')
        elif action == "withdraw":
            if balance > amount:
                balance -=amount
                print(f'current balance {balance}')
            else:
                print("insufficient balance")
        else:
            print("please enter withdraw or deposit properly")
    return inner

x=bank()
x()