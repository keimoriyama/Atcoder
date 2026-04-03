N, M = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, 0)

dp = [[-1000000000000000000] * (M + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if j == 0:
            dp[i][0] = 0
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + j * A[i])


print(dp[N][M])
