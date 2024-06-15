N, M = map(int, input().split())
S = []
for _ in range(N):
    S.append(input())

ans = 10000000000000
for i in range(1, 2**N):
    pat = []
    for j in range(N):
        if (i >> j) & 1:
            pat.append(j)
    f = [False] * M
    for p in pat:
        for m in range(M):
            if S[p][m] == "o":
                f[m] = True
    if False not in f:
        ans = min(ans, len(pat))


print(ans)
