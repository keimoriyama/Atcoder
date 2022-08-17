N, W = map(int, input().split())
A = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append([a, b])

A = sorted(A, key=lambda x: -x[0])

ans = 0
t_w = 0
for a in A:
    if t_w < W:
        ans += min(a[1], W-t_w) * a[0]
        t_w += min(a[1], W-t_w)

print(ans)
