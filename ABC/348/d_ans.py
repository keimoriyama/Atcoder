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
            A[i].append(0)
        elif aij == "T":
            ex = i
            ey = j
            A[i].append(0)
        elif aij == ".":
            A[i].append(0)
        elif aij == "#":
            A[i].append(-2)

N = int(input())
r, c, e = [], [], []
E = [[-1] * W for _ in range(H)]
for _ in range(N):
    ri, ci, ei = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)
    e.append(ei)
    E[ri - 1][ci - 1] = ei

used = [[False] * W for _ in range(H)]
q = deque()
q.append((sx, sy))
used[sx][sy] = True

dist = [[-1 for _ in range(W)] for _ in range(H)]
dist[sy][sx] = 0

while q:
    x, y = q.popleft()
    if E[x][y] <= dist[x][y]:
        continue
    dist[x][y] = E[x][y]
    queue = deque()
    queue.append((x, y))
    while queue:
        xi, yi = queue.popleft()
        for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ny = yi + dy
            nx = xi + dx
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if A[nx][ny] == -2:
                continue
            if dist[nx][ny] >= dist[xi][yi] - 1:
                continue
            dist[nx][ny] = dist[xi][yi] - 1
            queue.append((nx, ny))
            if not used[nx][ny]:
                used[nx][ny] = True
                q.append((nx, ny))


if dist[ex][ey] == -1:
    print("No")
else:
    print("Yes")
