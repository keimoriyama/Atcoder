from math import inf

X, Y, Z = map(int, input().split())
S = input()

dp = [[inf] * 2 for _ in range(len(S) + 1)]
dp[0][0] = 0
for i in range(len(S)):
    s = S[i]
    # capslockを入力した時の遷移
    dp[i][0] = min(dp[i][0], dp[i][1] + Z)
    dp[i][1] = min(dp[i][1], dp[i][0] + Z)

    if s == "a":
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + X)
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + Y)
    else:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + Y)
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + X)


print(min(dp[-1][0], dp[-1][1]))
