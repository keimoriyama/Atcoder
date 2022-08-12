N, Q = map(int, input().split())
A = list(map(int, input().split()))

B = []
ans = 0
for i in range(len(A) - 1):
    b = A[i + 1] - A[i]
    B.append(b)
    ans += abs(b)

for _ in range(Q):
    L, R, V = map(int, input().split())
    if L > 1:
        L -= 2
        ans -= abs(B[L])
        B[L] += V
        ans += abs(B[L])
    if R < N:
        R -= 1
        ans -= abs(B[R])
        B[R] -= V
        ans += abs(B[R])
    print(ans)
