N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
x, y = 0, 0
ans = 10**10
while (x < N) and (y < M):
    ans = min(ans, abs(A[x] - B[y]))
    if A[x] > B[y]:
        y += 1
    else:
        x += 1
print(ans)
