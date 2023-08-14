N, D = map(int, input().split())

S = [input() for _ in range(N)]

ans = 0
tmp = 0
for i in range(D):
    ok = True
    for j in range(N):
        if S[j][i] == "x":
            ok = False
    if ok:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0

print(max(ans, tmp))
