N, M = map(int, input().split())
g = [[-1] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    g[a][b] = c
    g[b][a] = c


ans = 0


def dfs(x, d, prev):
    global ans
    flag[x] = True
    for i, gi in enumerate(g[x]):
        if gi == -1 or flag[i]:
            continue
        ans = max(dfs(i, d + gi, x), ans)
    flag[x] = False
    return d


for i in range(1, N + 1):
    flag = [False] * (N + 1)
    dfs(i, 0, -1)
print(ans)
