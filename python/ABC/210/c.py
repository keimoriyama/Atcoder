N, K = map(int, input().split())
C = list(map(int, input().split()))

d = {}
for i in range(K):
    c = C[i]
    if c not in d.keys():
        d[c] = 1
    else:
        d[c] += 1

ans = len(d)

for i in range(K, N):
    c = C[i]
    c_k = C[i - K]
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1
    d[c_k] -= 1
    if d[c_k] == 0:
        del d[c_k]
    ans = max(ans, len(d))

print(ans)
