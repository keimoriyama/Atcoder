N, M = map(int, input().split())

B = []
for _ in range(N):
    B.append(list(map(int, input().split())))

x = [[0] * (M + 1) for _ in range(N + 1)]
y = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(M):
        x[i][j] = (B[i][j] + 6) // 7
        y[i][j] = (B[i][j] - 1) % 7 + 1

ans = "Yes"

for i in range(N):
    for j in range(M):
        if 0 < i and x[i][j] != x[i - 1][j] + 1:
            ans = "No"
        if 0 < j and y[i][j] != y[i][j - 1] + 1:
            ans = "No"
        if 0 < i and y[i][j] != y[i - 1][j]:
            ans = "No"
        if 0 < j and x[i][j] != x[i][j - 1]:
            ans = "No"


print(ans)
