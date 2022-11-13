N, M = map(int, input().split())
g = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(len(g)):
    g[i] = sorted(g[i])

for i in range(1, N + 1):
    a = g[i]
    d = len(a)
    print(d, end=" ")
    print(*a)
