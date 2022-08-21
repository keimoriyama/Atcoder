N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

l, r = -1, L + 1
while r > l + 1:
    mid = l + (r - l) // 2
    cnt, pre = 0, 0
    for i in range(N):
        if A[i] - pre >= mid and L - A[i] >= mid:
            cnt += 1
            pre = A[i]
    if cnt >= K:
        l = mid
    else:
        r = mid
print(l)
