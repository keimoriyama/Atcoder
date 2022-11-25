H, W = map(int, input().split())
C = []
for i in range(H):
    C.append(input())

f = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H - 1, -1, -1):
    for j in range(W - 1, -1, -1):
        if C[i][j] == "#":
            continue
        f[i][j] = max(f[i + 1][j], f[i][j + 1]) + 1
print(f[0][0])
