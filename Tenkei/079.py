H, W = map(int, input().split())

A, B = [], []
for _ in range(H):
    A.append(list(map(int, input().split())))

for _ in range(H):
    B.append(list(map(int, input().split())))

ans = 0
for i in range(H-1):
    for j in range(W-1):
        d = B[i][j] - A[i][j]
        A[i][j] += d
        A[i + 1][j] += d
        A[i][j + 1] += d
        A[i + 1][j + 1] += d
        ans += abs(d)
if A == B:
    print("Yes")
    print(ans)
else:
    print("No")
