N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        f = True
        Si = S[i]
        Sj = S[j]
        for si, sj in zip(Si, Sj):
            if si == "x" and sj == "x":
                f = False
        if f:
            ans += 1

print(ans)
