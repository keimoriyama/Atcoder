from collections import deque

N1, N2, M = map(int, input().split())
g = {i: [] for i in range(N1 + N2 + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


def bfs(start):
    dist = [-1] * (N1 + N2 + 1)
    q = deque()
    q.append(start)
    dist[start] = 0

    while len(q) > 0:
        x = q.popleft()
        for y in g[x]:
            if dist[y] != -1:
                continue
            dist[y] = dist[x] + 1
            q.append(y)
    return max(dist)


# print(g)
print(bfs(1) + bfs(N1 + N2) + 1)
