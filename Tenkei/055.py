N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            for l in range(k + 1, N):
                for m in range(l + 1, N):
                    a = (A[i] * A[j] * A[k] * A[l] * A[m]) % P
                    if a == Q:
                        ans += 1

print(ans)
