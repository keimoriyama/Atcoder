N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

t = 0
for i in range(N):
    t += A[i] / B[i]

t /= 2
ans = 0
for i in range(N):
    ans += min(A[i], t * B[i])
    t -= min(A[i] / B[i], t)

print(ans)
