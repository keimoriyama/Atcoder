H, W = map(int, input().split())
A = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)

row = []
for i in range(H):
    c = sum(A[i])
    row.append(c)

col = []
for i in range(W):
    c = 0
    for j in range(H):
        c += A[j][i]
    col.append(c)

B = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        ans = row[i] + col[j] - A[i][j]
        B[i][j] = str(ans)

for b in B:
    print(" ".join(b))
