from collections import deque

N = int(input())
c = 2010
G = [[0] * c for _ in range(c)]
edges = []
offset = 1005
for _ in range(N):
    x, y = map(int, input().split())
    x += offset
    y += offset
    G[x][y] = 1
    edges.append([x, y])

f = [[0] * c for _ in range(c)]
dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]
q = deque()
ans = 0
for x, y in edges:
    if f[x][y] == 1:
        continue
    ans += 1
    f[x][y] = 1
    q.append([x, y])
    while 0 < len(q):
        nx, ny = q.popleft()
        for i, j in zip(dx, dy):
            if G[nx + i][ny + j] == 1 and f[nx + i][ny + j] == 0:
                f[nx + i][ny + j] = 1
                q.append([nx + i, ny + j])

print(ans)
