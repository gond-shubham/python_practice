    def atm_simulation(x=0, type="deposit"):
    match type:
        case "deposit":
            deposit(x)
        case "withdraw":
            withdraw(x)
        case 'checkbalance':
            checkbalance()
        case _ :
            print("enter the valid type")


def deposit(a):
    global total_amount
    total_amount = total_amount + a
    print(f'{a} amount deposited')
    print(f'the total balance is {total_amount}')

def withdraw(a):
    global total_amount
    if a<=total_amount:
        total_amount = total_amount - a
        print(f'{a} amount withdrawed')
        print(f'the total balance is {total_amount}')
    else:
        print("insufficient balance")


def checkbalance():
    print(f'the balance is {total_amount}')

total_amount=5000

atm_simulation(500)