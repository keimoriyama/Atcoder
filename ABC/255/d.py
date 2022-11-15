from bisect import bisect_left

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
# ruiseki = [sum(A[:i]) for i in range(N + 1)]
ruiseki = [0]
for i in range(N):
    ruiseki.append(ruiseki[-1] + A[i])
for _ in range(Q):
    x = int(input())
    k = bisect_left(A, x)
    # print("k: {}".format(k))
    res = k * x - (N - k) * x - ruiseki[k] + ruiseki[-1] - ruiseki[k]
    # res -= (N - k) * x
    # res -= ruiseki[k]
    # res += ruiseki[-1] - ruiseki[k]
    print(res)
