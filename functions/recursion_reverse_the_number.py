def num_reverse(num):
    if num<10:
        return str(num)
    return str(num%10) + num_reverse(num//10)

print(num_reverse(int(input("enter the number:"))))
