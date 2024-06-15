N, A = map(int, input().split())
T = list(map(int, input().split()))
ans = 0
for t in T:
    if ans < t:
        ans = t + A
    else:
        ans += A
    print(ans)
