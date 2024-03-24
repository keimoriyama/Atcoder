H, W, M = map(int, input().split())

T, A, X = [], [], []
for i in range(M):
    t, a, x = map(int, input().split())
    T.append(t)
    A.append(a)
    X.append(x)

f = [False] * (H + 1)
g = [False] * (W + 1)
hc, wc = H, W

for i in range(M):
    A[i] -= 1

cnt = [0] * 200010

for i in range(M - 1, -1, -1):
    if T[i] == 1:
        if not f[A[i]]:
            hc -= 1
            f[A[i]] = True
            cnt[X[i]] += wc
    else:
        if not g[A[i]]:
            wc -= 1
            g[A[i]] = True
            cnt[X[i]] += hc

cnt[0] += wc * hc
ans = []

for i in range(len(cnt)):
    if cnt[i] != 0:
        ans.append([i, cnt[i]])

print(len(ans))
for a in ans:
    print(f"{a[0]} {a[1]}")
