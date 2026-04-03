N = int(input())

W, X = [], []
for _ in range(N):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)

ans = 0

for i in range(24):
    t = 0
    for j in range(N):
        if 9 <= (i + X[j]) % 24 < 18:
            t += W[j]
    # print(i, t)
    ans = max(ans, t)

print(ans)
