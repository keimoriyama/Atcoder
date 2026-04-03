from collections import deque

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
RCE = [list(map(int, input().split())) for _ in range(N)]

start_en = 0
for rcei in RCE:
    ri = rcei[0] - 1
    ci = rcei[1] - 1
    ei = rcei[2]
    A[ri][ci] = ei

# for ai in A:
#     print(ai)

q = deque()
q.append((sx, sy, -1, -1))
en = [[-1] * W for _ in range(H)]
en[sx][sy] = A[sx][sy]
flag = [[False] * W for _ in range(H)]
flag[sx][sy] = True

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


ans = False
while q:
    x, y, prev_x, prev_y = q.popleft()
    e = en[x][y]
    if e < 0:
        flag[x][y] = True
        continue
    for dxi, dyi in zip(dx, dy):
        xi = x + dxi
        yi = y + dyi
        if prev_x == xi and prev_y == yi:
            continue
        if xi < 0 or xi >= H or yi < 0 or yi >= W:
            continue
        if flag[xi][yi]:
            continue
        if A[xi][yi] == -2:
            continue
        if A[xi][yi] != -1:
            q.append((xi, yi, x, y))
            if A[xi][yi] == 0:
                en[xi][yi] = max(e - 1, en[xi][yi])
            else:
                en[xi][yi] = max(e + A[xi][yi], en[xi][yi])
        if sx == ex and sy == ey:
            ans = True
            break


print("Yes" if ans else "No")
