import itertools

N, M = map(int, input().split())

A = [[0] * N for _ in range(N)]
B = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A[a][b] = 1
    A[b][a] = 1

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    B[a][b] = 1
    B[b][a] = 1

ans = False
for p in itertools.permutations(range(N)):
    ok = True
    p = list(p)
    for i in range(N):
        for j in range(N):
            if A[i][j] != B[p[i]][p[j]]:
                ok = False
    if ok:
        ans = True

print("Yes" if ans else "No")
