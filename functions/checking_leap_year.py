def checkleap(year):
    if year %400 == 0:                     # the year should be divisible by 4 and not by 100
        print(f'{year} is leap year')      # if it's divisible by 4 and 100, then it must divisible by 400.
    elif year % 4 == 0 and year % 100 != 0:
        print(f'{year} is leap year')
    else:
        print(f'{year} is not leap year')


checkleap(int(input('enter the year')))