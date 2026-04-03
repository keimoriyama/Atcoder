T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    P = [i - 1 for i in P]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if P[i] > P[j]:
                break
        else:
            ans += 1
    print(ans)
