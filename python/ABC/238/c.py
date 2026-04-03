N = int(input())
L = len(str(N))
ans = 0

for i in range(1, L + 1):
    k = min(N, 10 ** i - 1) - (10 ** (i - 1) - 1)
    ans += k *(k + 1) // 2
    ans %= 998244353

print(ans)
