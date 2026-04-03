from collections import deque

N, M = map(int, input().split())
S = [input() for _ in range(N)]
flag = [[False] * M for _ in range(N)]
q = deque()
q.append((1, 1))
Dx = [0, 0, 1, -1]
Dy = [1, -1, 0, 0]
ans = 1

while len(q) > 0:
    x, y = q.popleft()
    flag[x][y] = True
    for dx, dy in zip(Dx, Dy):
        # "#"にぶつかるまで進む
        while S[x + dx][y + dy] == ".":
            x += dx
            y += dy
            if flag[x][y]:
                break
            ans += 1
    if not flag[x][y]:
        q.append((x, y))
    print(q)

print(ans)
