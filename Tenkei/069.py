def calc(x, n, m):
    ans = 1
    while n != 0:
        if n % 2 == 1:
            ans = ans * x % m
        x = x * x % m
        n = n // 2
    return ans


M = 1000000007

N, K = map(int, input().split())

if K == 1:
    if N == 1:
        print(1)
    else:
        print(0)
elif N == 1:
    print(K % M)
else:
    ans = K * (K-1) % M * calc(K-2, N-2, M)
    print(ans % M)
