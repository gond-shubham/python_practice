N = int(input())
M = list(map(int, input().split()))
Unique = set(M)

for i in Unique:
    if M.count(i) == 1:
        print(i)
