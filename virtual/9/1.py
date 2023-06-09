H, W = map(int, input().split())
S = [input() for _ in range(H)]

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, 1, -1, 0, 1, -1, 0, 1]
ans = []
for y in range(H):
    d = []
    for x in range(W):
        cnt = 0
        for i in range(len(dx)):
            _dx = x + dx[i]
            _dy = y + dy[i]
            if _dx < 0 or _dx >= W:
                continue
            if _dy < 0 or _dy >= H:
                continue
            if S[_dy][_dx] == "#":
                cnt += 1
        d.append(cnt)
    ans.append(d)


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            print("#", end="")
        else:
            print(ans[i][j], end="")
    print()
