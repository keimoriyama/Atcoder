from collections import deque

Dx, Dy = [0, 0, 1, -1], [1, -1, 0, 0]


H, W = map(int, input().split())
A = [[] for _ in range(H)]
sx, sy = -1, -1
ex, ey = -1, -1
for i in range(H):
    ai = input()
    for j, aij in enumerate(ai):
        if aij == "S":
            sx = i
            sy = j
            A[i].append(-1)
        elif aij == "T":
            ex = i
            ey = j
            A[i].append(-1)
        elif aij == ".":
            A[i].append(0)
        elif aij == "#":
            A[i].append(-2)

N = int(input())
r, c, e = [], [], []
for _ in range(N):
    ri, ci, ei = map(int, input().split())
    r.append(ri)
    c.append(ci)
    e.append(ei)


def bfs(x, y):
    q = deque()
    q.append((x, y))
    dist = [[10**100] * W for _ in range(H)]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(Dx, Dy):
            xi = x + dx
            yi = y + dy
            if xi < 0 or xi >= H or yi < 0 or yi >= W:
                continue
            if A[xi][yi] == -2:
                continue
            if dist[xi][yi] > dist[x][y] + 1:
                dist[xi][yi] = dist[x][y] + 1
                q.appendleft((xi, yi))
    return dist


isReachable = [[False] * N for _ in range(N)]
for i in range(N):
    dist = bfs(r[i], c[i])
    for j in range(N):
        if dist[r[j]][c[j]] <= e[i]:
            isReachable[i][j] = True
