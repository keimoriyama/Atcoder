from bisect import bisect_left, bisect_right

N = int(input())
A = [-1] + list(map(int, input().split()))
Q = int(input())
sleep = [0]
for i in range(1, len(A) // 2):
    sleep.append(sleep[-1] + A[2 * i + 1] - A[2 * i])

# print(sleep)
for _ in range(Q):
    l, r = map(int, input().split())
    ans = 0
    li = bisect_left(A, l) - 1
    ri = bisect_left(A, r) - 1
    if li % 2 == 0:
        ans += A[li + 1] - l
    if ri % 2 == 0:
        ans -= A[ri + 1] - r

    # print(li, ri, sleep[li // 2], sleep[ri // 2], A[li], A[ri])
    ans += sleep[ri // 2] - sleep[li // 2]
    print(ans)
