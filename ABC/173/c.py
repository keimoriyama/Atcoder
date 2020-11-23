def count(matrix):
    ans = 0
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == '#':
                ans += 1
    return ans


def solve(matrix, i, j):
    result = 0
    ans = 0
    """
    for i in range(H):
        for j in range(W):
            matrix[i][j] = 0
            result = count(matrix)
            if result > K:
                ans += 1
    """
    if (i < H) and (j < W):
        s = matrix[i][j]
        matrix[i][j] = 0
        result = count(matrix)
        if result == K:
            ans += 1
        solve(matrix, i+1, j)
        matrix[i][j] = s
        solve(matrix, i, j+1)
        matrix[i][j] = s
    else:
        return
    return ans


H, W, K = map(int, input().split())
list = []
list2 = []
for i in range(H):
    a = input()
    for j in range(W):
        list.append(a[j])

for i in range(H):
    list2.append(list[i*W:i*W+W])

ans = 0
print(list2)


print(count(list2))

print(solve(list2, 0, 0))
