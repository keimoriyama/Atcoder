N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

dp = [[0] * (2) for _ in range(N + 1)]


for i in range(N):
    x, y = X[i], Y[i]
    # 料理が解毒料理の場合
    if x == 0:
        # 解毒されるまたは、お腹を壊していなくて食べない
        dp[i + 1][0] = max(max(dp[i][1], dp[i][0]) + y, dp[i][0])
    # 料理に毒がある場合
    else:
        # お腹を壊していない時に料理を食べるかお腹を壊している時に料理を下げるかのどちらか
        dp[i + 1][1] = max(dp[i][0] + y, dp[i][1])
    # 食べない場合
    dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])
    dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])
    # print(x, y)
    # print(dp)
    # print()


print(max(dp[-1]))
