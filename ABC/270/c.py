from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(n, to):
    global stop
    if not stop:
        q.append(n)
    if n == to:
        stop = True
    f[n] = 1
    for e in T[n]:
        if f[e] == 1:
            continue
        dfs(e, to)
    if not stop:
        q.pop()


N, X, Y = map(int, input().split())

T = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    T[u].append(v)
    T[v].append(u)


f = [0] * (N + 1)
stop = False
q = deque()

dfs(X, Y)

print(*q)
