N, K = map(int, input().split())

v = []
for _ in range(N):
    a, b = map(int, input().split())
    v.append(b)
    v.append(a - b)

v = list(reversed(sorted(v)))
ans = 0
for i in v[:K]:
    ans += i

print(ans)
