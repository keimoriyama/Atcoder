from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
C = [A[i] - (i + 1) for i in range(N)]

for _ in range(Q):
    k = int(input())
    i = bisect_left(C, k)
    if i == N:
        print(A[N - 1] + (k - C[N - 1]))
    else:
        print(A[i] - (C[i] - k + 1))
