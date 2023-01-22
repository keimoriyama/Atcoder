N, K, D = map(int, input().split())

A = list(map(int, input().split()))

dp = [[[-1] * D for i in range(K + 1)] for i in range(N + 1)]
dp[1][1][A[0] % D] = A[0]
for i in range(1, N):
    a = A[i]
    dp[i + 1][1][a % D] = max(dp[i][1][a % D], a)
    for j in range(K + 1):
        for l in range(D):
            if dp[i][j][l] == -1:
                continue
            dp[i + 1][j][l] = max(dp[i][j][l], dp[i + 1][j][l])
            if j == K:
                continue
            dp[i + 1][j + 1][(l + a) % D] = max(
                dp[i][j][l] + a, dp[i + 1][j + 1][(l + a) % D]
            )

print(dp[N][K][0])
