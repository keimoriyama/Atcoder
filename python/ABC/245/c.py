import numpy as np

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(N + 1)]
dp[0][0] = 1
dp[0][1] = 1

for i in range(N - 1):
    for j in range(2):
        # print(dp)
        if dp[i][j] == 0:
            continue
        x_i = 0
        if j == 0:
            x_i = A[i]
        else:
            x_i = B[i]
        # print(x_i, A[i + 1], B[i + 1])
        if abs(x_i - A[i + 1]) <= K:
            dp[i + 1][0] = 1
        if abs(x_i - B[i + 1]) <= K:
            # print(x_i, A[i + 1], B[i + 1])
            dp[i + 1][1] = 1

if dp[N - 1][0] == 1 or dp[N - 1][1] == 1:
    print("Yes")
else:
    print("No")
