def generate_primenum():
    n=2
    while True:
        count =0
        for i in range(1, n+1):
            if n % i == 0:
                count =count+1
        if count ==2:
            yield n
        n+=1


p= generate_primenum()

for i in p:
    print(i)