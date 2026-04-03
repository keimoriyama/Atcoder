import sys
from collections import defaultdict

sys.setrecursionlimit(10**8)
N = int(input())
g = {}

for _ in range(N):
    s, t = input().split()
    g[s] = t
# ループがあるかどうかを検出する
flag = defaultdict(bool)
done = defaultdict(bool)


def dfs(i):
    flag[i] = True
    if i in g:
        if not flag[g[i]]:
            dfs(g[i])
        elif not done[g[i]]:
            print("No")
            exit()
    done[i] = True


for s in g.keys():
    if flag[s]:
        continue
    dfs(s)

print("Yes")
