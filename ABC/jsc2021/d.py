N, P = map(int, input().split())

mod = 1000000007
ans = (P - 1) * pow(P - 2, N - 1, mod) % mod
print(ans)
