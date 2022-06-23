import math
N, K = map(int, input().split())
A = list(map(int, input().split()))

p = [[0, 0]]

for _ in range(N):
    x, y = map(int, input().split())
    p.append([x, y])

dist = [[0] * (N + 1) for i in range(K)]

for g in range(K):
    for r in range(1, N+1):
        dist[g][r] = math.sqrt((p[g][0] - p[r][0]) ** 2 + (p[g][1] - p[r][1]) ** 2)

R_min = [0] * (N+1)

for r in range(1, N+1):
    d = math.inf
    for g in range(K):
        d = min(d, dist[g][r])
    R_min[r] = d

print(max(R_min))
