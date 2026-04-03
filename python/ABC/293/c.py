H, W = map(int, input().split())

A = []
for _ in range(H):
    A.append(list(map(int, input().split())))
ans = 0


def dfs(x, y, nums):
    global ans
    if A[x][y] in nums:
        return
    nums.add(A[x][y])
    if x == H - 1 and y == W - 1:
        ans += 1
    if 0 <= x + 1 < H:
        dfs(x + 1, y, nums)
    if 0 <= y + 1 < W:
        dfs(x, y + 1, nums)
    nums.remove(A[x][y])


dfs(0, 0, set())
print(ans)
