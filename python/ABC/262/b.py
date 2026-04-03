N, M = map(int, input().split())
g = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    g[u][v] = 1
    g[v][u] = 1

ans = 0
for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if g[a][b] == 1 and g[b][c] == 1 and g[a][c] == 1:
                ans += 1

print(ans)