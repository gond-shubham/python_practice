def evenodd(object):
    ce=0
    co =0
    for i in object:
        if i %2 ==0:
            ce+=1
        else:
            co+=1
    print(f'the even count is {ce}')
    print(f'the odd count is {co}')

evenodd([29,34,6,7,99,12,0])