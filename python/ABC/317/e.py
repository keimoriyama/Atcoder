from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
s, g = [], []
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            s = [i, j, 0]
        elif A[i][j] == "G":
            g = [i, j]
        elif A[i][j] == "<":
            for k in reversed(range(0, j)):
                if A[i][k] == "." or A[i][k] == "!":
                    A[i][k] = "!"
                else:
                    break
        elif A[i][j] == ">":
            for k in range(j + 1, W):
                if A[i][k] == "." or A[i][k] == "!":
                    A[i][k] = "!"
                else:
                    break
        elif A[i][j] == "^":
            for k in reversed(range(0, i)):
                if A[k][j] == "." or A[k][j] == "!":
                    A[k][j] = "!"
                else:
                    break
        elif A[i][j] == "v":
            for k in range(i + 1, H):
                if A[k][j] == "." or A[k][j] == "!":
                    A[k][j] = "!"
                else:
                    break
flag = [[-1] * W for _ in range(H)]
q = deque()

q.append(s)
Dx = [0, 0, -1, 1]
Dy = [-1, 1, 0, 0]
p = []
while len(q) > 0:
    x, y, d = q.popleft()
    flag[x][y] = d
    for dx, dy in zip(Dx, Dy):
        if x + dx < 0 or x + dx >= H or y + dy < 0 or y + dy >= W:
            continue
        if flag[x + dx][y + dy] != -1 or A[x + dx][y + dy] not in [".", "G", "S"]:
            continue
        flag[x + dx][y + dy] = True
        q.appendleft((x + dx, y + dy, d + 1))


# for f in flag:
#     print(f)

print(flag[g[0]][g[1]])
