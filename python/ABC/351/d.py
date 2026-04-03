from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

Dx, Dy = [0, 0, -1, 1], [-1, 1, 0, 0]
ans = 0
for i in range(H):
    for j in range(W):
        flag = [[False] * W for _ in range(H)]
        q = deque()
        q.append((i, j))
        free, magnet = 0, False
        while q:
            q_i = q.popleft()
            x, y = q_i[0], q_i[1]
            flag[x][y] = True
            free += 1
            # 周囲の点を探索
            for dx, dy in zip(Dx, Dy):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < H) or not (0 <= ny < W):
                    continue
                if S[nx][ny] == "#" or flag[nx][ny]:
                    continue
                else:
                    q.append((nx, ny))
        ans = max(ans, free)
        print(i, j, free)

print(ans)
