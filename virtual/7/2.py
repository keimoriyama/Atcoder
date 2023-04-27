from collections import deque

N = int(input())

c = 2010
G = [[0] * c for _ in range(c)]

p = []
for _ in range(N):
    x, y = map(int, input().split())
    x += 1005
    y += 1005
    G[x][y] = 1
    p.append((x, y))

f = [[False] * c for _ in range(c)]
count = 0

Dx = [-1, -1, 0, 0, 1, 1]
Dy = [-1, 0, -1, 1, 0, 1]

ans = 0
f = [[False] * c for _ in range(c)]
for point in p:
    x = point[0]
    y = point[1]
    if f[x][y]:
        continue
    q = deque()
    q.append([x, y])
    f[x][y] = True
    ans += 1
    while q:
        x, y = q.popleft()
        count += 1
        for dx, dy in zip(Dx, Dy):
            nx = x + dx
            ny = y + dy
            if G[nx][ny] == 1 and not f[nx][ny]:
                f[nx][ny] = True
                q.append([nx, ny])


print(ans)
