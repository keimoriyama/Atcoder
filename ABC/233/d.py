from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
A_r = [0] * (N + 1)
for i in range(N):
    A_r[i + 1] = A_r[i] + A[i]

ans = 0
for i in range(1, N + 1):
    d[A_r[i - 1]] += 1
    ans += d[A_r[i] - K]

print(ans)
