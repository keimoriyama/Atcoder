N, M = map(int, input().split())

ans = 2e18
for a in range(1, N + 1):
    b = (M + a - 1) // a
    if b <= N:
        ans = min(ans, a * b)
    if a > b:
        break

if ans == 2e18:
    print(-1)
else:
    print(ans)
