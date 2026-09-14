T = int(input())

for i in range(T):
    s_c = 0
    l_c = 0
    m = int(input())
    N = input().split()
    print(N, type(N))
    for j in range(m):
        if N[j] == "START38":
            s_c +=1
        else:
            l_c+=1
    print(s_c, l_c)
        
