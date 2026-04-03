T = int(input())
for _ in range(T):
    t = int(input())
    case = list(map(int, input().split()))
    ans = 0
    for c in case:
        if c % 2 == 1:
            ans += 1
    print(ans)
