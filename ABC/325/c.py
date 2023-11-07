from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

Dx = [-1, 0, 1, -1, 1, -1, 0, 1]
Dy = [1, 1, 1, 0, 0, -1, -1, -1]

flag = [[False] * W for _ in range(H)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        flag[x][y] = True
        for dx, dy in zip(Dx, Dy):
            if x + dx < 0 or x + dx >= H or y + dy < 0 or y + dy >= W:
                continue
            if flag[x + dx][y + dy]:
                continue
            if S[x + dx][y + dy] == "#":
                q.appendleft((x + dx, y + dy))


ans = 0
for i in range(H):
    for j in range(W):
        if flag[i][j]:
            continue

        if S[i][j] == "#":
            bfs(i, j)
            ans += 1

print(ans)
