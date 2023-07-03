from collections import deque

H, W = map(int, input().split())
s = [input() for _ in range(H)]

n = 0
for si in s:
    for sj in si:
        if sj == "#":
            n += 1

q = deque()
q.append((0, 0))

m = [[-1] * W for _ in range(H)]
m[0][0] = 1

Dx = [-1, 1, 0, 0]
Dy = [0, 0, -1, 1]

while len(q) > 0:
    x, y = q.popleft()
    if x == H - 1 and y == W - 1:
        break
    for dx, dy in zip(Dx, Dy):
        ndx = x + dx
        ndy = y + dy
        # print(ndx, ndy)
        if 0 <= ndx < H and 0 <= ndy < W:
            if s[ndx][ndy] == "#":
                continue
            if m[ndx][ndy] == -1:
                m[ndx][ndy] = m[x][y] + 1
                q.append((ndx, ndy))
if m[H - 1][W - 1] == -1:
    print(-1)
else:
    print(H * W - n - m[H - 1][W - 1])
