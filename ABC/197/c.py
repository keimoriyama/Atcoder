N = int(input())
a = list(map(int, input().split()))

ans = float("inf")
for b in range(1 << (N - 1)):
    s = 0
    t = 0
    for i in range(N):
        t |= a[i]
        if i == N - 1:
            continue
        if 1 & (b >> i):
            s ^= t
            t = 0
    if t:
        s ^= t
    ans = min(ans, s)

print(ans)
