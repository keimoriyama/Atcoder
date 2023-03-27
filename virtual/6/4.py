from collections import deque

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())


def set_dist():
    return [[-1] * W for _ in range(H)]


def bfs(i, j, dist):
    Dx = [0, 0, 1, -1]
    Dy = [1, -1, 0, 0]
    q = deque()
    q.append([i, j])
    dist[i][j] = 0
    res = -1
    while len(q) > 0:
        x, y = q.popleft()
        res = max(res, dist[x][y])
        for dx, dy in zip(Dx, Dy):
            if x + dx < 0 or x + dx >= H:
                continue
            if y + dy < 0 or y + dy >= W:
                continue
            if S[x + dx][y + dy] == "#":
                continue
            if dist[x + dx][y + dy] == -1:
                dist[x + dx][y + dy] = dist[x][y] + 1
                q.append([x + dx, y + dy])
    return res


ans = -1
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        dist = set_dist()
        res = bfs(i, j, dist)
        ans = max(ans, res)
print(ans)
