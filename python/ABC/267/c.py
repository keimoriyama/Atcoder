N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for i in range(len(A)):
    S.append(S[-1] + A[i])

n = 0
for i in range(0, M):
    n += A[i] * (i + 1)

sumi = [0] * (N - M + 1)
sumi[0] = n
for i in range(1, N - M + 1):
    sumi[i] = sumi[i - 1] + M * A[M + i - 1] - (S[M + i - 1] - S[i - 1])

ans = -1000000000000000000
for i in range(N - M + 1):
    ans = max(ans, sumi[i])
print(ans)
