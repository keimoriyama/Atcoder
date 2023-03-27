from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

p = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        p.append([i, j])

Dx = [0, 0, 1, -1]
Dy = [1, -1, 0, 0]
ans = 0
for i in range(len(p)):
    flag = [[False] * W for _ in range(H)]
    dist = [[-1] * W for _ in range(H)]
    dist[p[i][0]][p[i][1]] = 0
    q = deque()
    q.append(p[i])
    while q:
        point = q.popleft()
        x = point[0]
        y = point[1]
        flag[x][y] = True
        for dx, dy in zip(Dx, Dy):
            if (0 <= x + dx < H) and (0 <= y + dy < W):
                if flag[x + dx][y + dy] or S[x + dx][y + dy] == "#":
                    continue
                flag[x + dx][y + dy] = True
                dist[x + dx][y + dy] = dist[x][y] + 1
                q.append([x + dx, y + dy])
    ans = max(ans, max(max(dist)))

print(ans)
