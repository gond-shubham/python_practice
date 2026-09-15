def maxi(num1, num2, num3):
    if num1>=num2:
        if num1>=num3:
            print(f'{num1} is greater')
        else:
            print(f'{num3} is greater')
    elif num2>=num3:
        print(f'{num2} is greater')
    else:
        print(f'{num3} is greater')



maxi(2, 5, 5)