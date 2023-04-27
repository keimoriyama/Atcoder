N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]


for _ in range(N):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u][v] += 1

for g in G:
    print(g)
