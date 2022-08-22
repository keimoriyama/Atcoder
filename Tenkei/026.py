import sys
from tempfile import tempdir

sys.setrecursionlimit(10**6)
N = int(input())
t = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    t[a].append(b)
    t[b].append(a)

c1, c2 = [], []
f = [0] * (N + 1)
color = [0] * (N + 1)


def dfs(pos):
    f[pos] = 1
    for i in t[pos]:
        if f[i] == 1:
            continue
        color[i] = 1 - color[pos]
        dfs(i)


dfs(1)
for i, c in enumerate(color):
    if i == 0:
        continue
    if c == 0:
        c1.append(i)
    else:
        c2.append(i)

if len(c1) >= len(c2):
    print(*c1[: N // 2])
else:
    print(*c2[: N // 2])
