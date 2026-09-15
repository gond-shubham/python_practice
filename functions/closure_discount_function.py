def discount(dis_per=10):
    def inner(total_amount):
       return total_amount/100 * (100 - dis_per)
    return inner


y = discount()
print(y(175))


