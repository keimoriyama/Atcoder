N, X = map(int, input().split())

A = list(map(int, input().split()))
A.insert(0, 0)
f = [0] * (len(A) + 1)

ans = 0
next = X
while f[next] != 1:
    f[next] = 1
    next = A[next]
    ans += 1

print(ans)
