print("**************************************")
while True:
    n1=int(input("Enter First Number :"))
    n2=int(input("Enter Second Number :"))
    try:
        n3=n1/n2
        print(n1,n2,n3,n4)
        break
    except ZeroDivisionError:
        print("cannot divide number with zero try again...")
