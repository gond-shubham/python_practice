M = int(input())
Mset = set(map(int, input().split()))

N = int(input())
Nset = set(map(int, input().split()))

C = sorted(Mset.symmetric_difference(Nset))

print(C)
