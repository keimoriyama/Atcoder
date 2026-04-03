from bisect import bisect_left

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

for _ in range(Q):
    x = int(input())
    center = bisect_left(A, x)
    ans = len(A) - center
    print(ans if ans > 0 else 0)
