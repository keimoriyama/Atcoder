N, X = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [[0] * (X + 1) for i in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    for j in range(0, X):
        if dp[i][j] != 1:
            continue
        if j + A[i] <= X:
            dp[i + 1][j + A[i]] = 1
        if j + B[i] <= X:
            dp[i + 1][j + B[i]] = 1


if dp[N][X] == 1:
    print("Yes")
else:
    print("No")
