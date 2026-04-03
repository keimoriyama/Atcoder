import sys

N, M = map(int, input().split())
sys.setrecursionlimit(1000 + N)
G = {i: [] for i in range(N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

color = [0] * (N + 1)


def dfs(v, p, c):
    r = [0, 0]
    color[v] = c
    if c == 1:
        r[0] += 1
    else:
        r[1] += 1
    for g in G[v]:
        if g == p or color[g] == -c:
            continue
        if color[g] == c:
            return [-1, -1]
        res = dfs(g, v, -c)

        if res[1] == -1:
            return [-1, -1]
        r[1] += res[1]
        r[0] += res[0]
    return r


ans = N * (N - 1) // 2 - M
for i in range(1, N + 1):
    if color[i]:
        continue
    res = dfs(i, -1, 1)
    if res[0] == -1:
        print(0)
        exit()
    ans -= res[0] * (res[0] - 1) // 2
    ans -= res[1] * (res[1] - 1) // 2

print(ans)
