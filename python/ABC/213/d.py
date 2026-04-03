import sys

sys.setrecursionlimit(10**9)
N = int(input())
G = [[] for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

route = []
for i in range(N + 1):
    G[i].sort()


def dfs(i, prev):
    route.append(i)
    for g in G[i]:
        if g != prev:
            dfs(g, i)
            route.append(i)


dfs(1, -1)
print(*route)
