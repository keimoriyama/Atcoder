N, P = map(int, input().split())
A = list(map(int, input().split()))

n = 0
for a in A:
    if a >= P:
        continue
    n += 1

print(n)
