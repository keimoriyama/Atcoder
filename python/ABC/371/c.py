from itertools import permutations

N = int(input())
Mg = int(input())
Gg = [[0] * N for _ in range(N)]
for i in range(Mg):
    u, v = map(int, input().split())
    Gg[u - 1][v - 1] = Gg[v - 1][u - 1] = 1

Mh = int(input())
Gh = [[0] * (N) for _ in range(N)]
for i in range(Mh):
    u, v = map(int, input().split())
    Gh[u - 1][v - 1] = Gh[v - 1][u - 1] = 1

A = []
for i in range(N - 1):
    row = list(map(int, input().split()))
    A.append([0] * (i + 1) + row)
ans = 10**9
for p in permutations(range(N)):
    cost = 0
    for i in range(N):
        for j in range(i + 1, N):
            if Gg[p[i]][p[j]] ^ Gh[i][j]:
                cost += A[i][j]
    ans = min(ans, cost)
print(ans)
