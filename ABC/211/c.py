S = input()
N = len(S)
T = "#chokudai"

dp = [[0] * (9) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = 1

for i in range(N):
    for j in range(1, 9):
        if S[i] != T[j]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

print(dp[N - 1][8] % (10**9 + 7))
