N, M = map(int, input().split())
S, C = [], []
for _ in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

for i in range(10**N + 1):
    si = str(i)
    ok = True
    if len(si) < N:
        continue
    for j in range(M):
        if si[S[j] - 1] != str(C[j]):
            ok = False
    if ok:
        print(si)
        exit()


print(-1)
