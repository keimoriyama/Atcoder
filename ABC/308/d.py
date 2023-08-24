from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]
p = ["s", "n", "u", "k", "e"]

q = deque([(0, 0, 1)])

flag = [[False] * W for _ in range(H)]
Dx = [0, 0, 1, -1]
Dy = [-1, 1, 0, 0]


while q:
    x, y, c = q.popleft()
    flag[x][y] = True
    for dx, dy in zip(Dx, Dy):
        if 0 > x + dx or x + dx >= H or 0 > y + dy or W <= y + dy:
            continue
        if flag[x + dx][y + dy]:
            continue
        if S[x + dx][y + dy] == p[c % 5]:
            # print(p[c % 5], c % 5)
            # print(q)
            flag[x + dx][y + dy] = True
            q.append((x + dx, y + dy, c + 1))

# for i in range(H):
#     for j in range(W):
#         print(S[i][j] if flag[i][j] else "0", end=" ")
#     print()
print("Yes" if flag[-1][-1] else "No")
