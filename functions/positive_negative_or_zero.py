def valuecheck(num):
    if num>0:
        print(f'the given number {num} is positive')
    elif num<0:
        print(f'the given number {num} is negative')
    else:
        print(f'the given number {num} is zero')


valuecheck(int(input("enter the number")))