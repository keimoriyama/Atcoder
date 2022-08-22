from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs -= 1
cs -= 1
rt -= 1
ct -= 1
S = []
for _ in range(H):
    S.append(input())

d = deque()
dist = [[[pow(10, 6)] * 4 for _ in range(W)] for _ in range(H)]
for i in range(4):
    dist[rs][cs][i] = 0
    d.append([rs, cs, i])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while d:
    x, y, direct = d.popleft()
    cx = x + dx[direct]
    cy = y + dy[direct]
    if 0 <= cx < H and 0 <= cy < W and S[cx][cy] == ".":
        for i in range(4):
            t = 0 if i == direct else 1
            if dist[cx][cy][i] > dist[cx][cy][direct] + t:
                dist[cx][cy][i] = dist[cx][cy][direct] + t
                if t == 0:
                    d.appendleft([cx, cy, i])
                else:
                    d.append([cx, cy, i])
print(min(dist[rt][ct]))
