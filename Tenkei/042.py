K = int(input())
if K % 9 != 0:
    print(0)
    exit()
dp = [0] * (K + 1)
dp[0] = 1
for i in range(1, K + 1):
    j = i - 1
    while j >= i - 9 and j >= 0:
        dp[i] += dp[j]
        j -= 1

print(dp[K] % (10**9 + 7))
