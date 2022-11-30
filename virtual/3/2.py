from itertools import permutations

N, M = map(int, input().split())

f1 = [[False] * (10) for _ in range(10)]
f2 = [[False] * (10) for _ in range(10)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    f1[a][b] = True
    f1[b][a] = True
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    f2[a][b] = True
    f2[b][a] = True

f = False
for v in permutations(range(N)):
    p = True
    for i in range(N):
        for j in range(N):
            if f1[i][j] != f2[v[i]][v[j]]:
                p = False
    if p:
        f = True
if f:
    print("Yes")
else:
    print("No")
