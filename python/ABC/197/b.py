H, W, X, Y = map(int, input().split())

grid = []

for i in range(H):
    grid.append(list(input()))

X -= 1
Y -= 1

ans = 0

# 上
for i in range(1, H):
    if 0 <= X - i:
        if grid[X - i][Y] == ".":
            ans += 1
        else:
            break
# 下
for i in range(1, H):
    if X + i < H:
        if grid[X + i][Y] == "#":
            break
        else:
            ans += 1
# 左
for i in range(1, W):
    if 0 <= Y - i < W:
        if grid[X][Y - i] == "#":
            break
        else:
            ans += 1
# 右
for i in range(1, W):
    if 0 <= Y + i < W:
        if grid[X][Y + i] == "#":
            break
        else:
            ans += 1

ans += 1

print(ans)
