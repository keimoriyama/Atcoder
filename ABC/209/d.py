import sys

sys.setrecursionlimit(10**9)


def dfs(i, c):
    if flag[i]:
        return
    flag[i] = True
    if c == 0:
        color[i] = 1
    else:
        color[i] = 0
    for g in G[i]:
        if c == 0:
            dfs(g, 1)
        else:
            dfs(g, 0)


N, Q = map(int, input().split())
G = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

flag = [False] * (N + 1)
color = [-1] * (N + 1)
dfs(1, 0)
for _ in range(Q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
