N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(list(map(int, input().split())))
X = int(input())

dp = [False] * (X + 1)
dp[0] = True

for i in range(X + 1):
    for a in A:
        # 範囲外
        if i + a > X:
            continue
        # もちがある
        if (i + a) in B:
            continue
        if dp[i]:
            dp[i + a] = True

if dp[X]:
    print("Yes")
else:
    print("No")
