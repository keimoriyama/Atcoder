from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
k = defaultdict(int)
for a in A:
    k[a] += 1

k = sorted(k.items(), reverse=True)
i = 0

for v in k:
    print(v[1])
    i += 1
for j in range(i, N):
    print(0)
