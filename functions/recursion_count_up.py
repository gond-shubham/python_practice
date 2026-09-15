def count_up(num):
    if num ==1:
        print(1)
        return
    count_up(num-1)
    print(num)


count_up(10)

