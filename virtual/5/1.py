N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)
k_num = 0
for i in range(len(A)):
    k = A[i] // X
    k_num += k

n = min(k_num, K)
ans -= n * X
K -= n

A = [a % X for a in A]
A = sorted(A, reverse=True)
for a in A:
    if K <= 0:
        break
    ans -= min(a, X)
    K -= 1

print(ans)
