N, M = map(int, input().split())
A = list(map(int, input().split()))
maxA = max(max(A), M)

k = [True] * (maxA + 1)
isprime = [True] * (maxA + 1)
prime = []
for a in A:
    k[a] = False

for i in range(2, maxA + 1):
    if not isprime[i]:
        continue
    for j in range(i * 2, maxA + 1, i):
        isprime[j] = False
        k[i] = k[i] and k[j]
    if not k[i]:
        prime.append(i)

for p in prime:
    for j in range(p * 2, M + 1, p):
        k[j] = k[j] and k[p]

ans = [1]
for i in range(2, M + 1):
    if k[i]:
        ans.append(i)

print(len(ans))
for a in ans:
    print(a)
