N, M = map(int, input().split())
G = {i: [] for i in range(N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

flag = [False] * (N + 1)

ans = 0


def dfs(i):
    flag[i] = True
    for g in G[i]:
        if flag[g]:
            continue
        dfs(g)


col = 0
for i in range(1, N + 1):
    if flag[i]:
        continue
    dfs(i)
    ans += 1

print(ans)
