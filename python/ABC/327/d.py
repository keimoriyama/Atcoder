import collections
import sys

sys.setrecursionlimit(100100100)


def dfs(c, x):
    global b
    X[c] = x
    for d in g[c]:
        if X[d] == -1:
            dfs(d, 1 - x)
        elif X[d] == X[c]:
            b = False


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

g = collections.defaultdict(list)

for i in range(M):
    a, b = A[i], B[i]
    g[a].append(b)
    g[b].append(a)

X = [-1] * (N + 1)
b = True
for i in range(1, N + 1):
    if X[i] == -1:
        dfs(i, 0)

print("Yes" if b else "No")
