def GST(amt, a=18):
    A= a/100*amt
    return A
def discount(amt, a= 10):
    A= a/100*amt
    return A

def final_bill():
    amt = int(input("enter the value"))
    total = amt + GST(amt) - discount(amt)
    print(total)

final_bill()