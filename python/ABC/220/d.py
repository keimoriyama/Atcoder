N = int(input())
A = list(map(int, input().split()))

dp = [[0] * (10) for _ in range(N)]

dp[0][A[0]] = 1

for i in range(1, N):
    for j in range(10):
        f = (j + A[i]) % 10
        g = (j * A[i]) % 10
        dp[i][f] += dp[i - 1][j]
        dp[i][g] += dp[i - 1][j]
        dp[i][f] %= 998244353
        dp[i][g] %= 998244353

for i in range(10):
    print(dp[N - 1][i])
