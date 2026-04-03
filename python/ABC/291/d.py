M = 998244353
N = int(input())

card = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]
dp[0] = [1, 1]


for i in range(1, N):
    for pre in range(2):
        for nex in range(2):
            if card[i - 1][pre] != card[i][nex]:
                dp[i][nex] += dp[i - 1][pre]
    dp[i][0] %= M
    dp[i][1] %= M

print((dp[N - 1][0] + dp[N - 1][1]) % M)
