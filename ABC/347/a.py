N, K = map(int, input().split())
A = list(map(int, input().split()))

for ai in A:
    if ai % K == 0:
        print(ai // K, end=" ")

print()
