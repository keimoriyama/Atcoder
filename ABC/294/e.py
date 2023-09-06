L, N1, N2 = map(int, input().split())
x1 = [list(map(int, input().split())) for _ in range(N1)]
x2 = [list(map(int, input().split())) for _ in range(N2)]

ans = 0
ni, nj = 0, 0
p, q = 0, 0
while (ni < N1) and (nj < N2):
    if x1[ni][0] == x2[nj][0]:
        ans += min(p + x1[ni][1], q + x2[nj][1]) - max(p, q)
    if p + x1[ni][1] < q + x2[nj][1]:
        p += x1[ni][1]
        ni += 1
    else:
        q += x2[nj][1]
        nj += 1

print(ans)
