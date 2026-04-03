N = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(N):
    min_a = A[l]
    for r in range(l, N):
        min_a = min(min_a, A[r])
        ans = max(ans, min_a * (r - l + 1))

print(ans)
