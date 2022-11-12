import sys

sys.setrecursionlimit(100000000)
N = int(input())
G = [[] for _ in range(int(2e5))]
idx2node = {1: 1}
i = 1
for _ in range(N):
    a, b = map(int, input().split())
    if a not in idx2node.keys():
        idx2node[a] = i + 1
        i += 1
    if b not in idx2node.keys():
        idx2node[b] = i + 1
        i += 1
    G[idx2node[a]].append(idx2node[b])
    G[idx2node[b]].append(idx2node[a])

flag = [False] * (len(idx2node) + 1)
node2idx = {v: k for v, k in zip(idx2node.values(), idx2node.keys())}
point = -1


def dfs(i):
    global point
    if flag[i]:
        return
    if point < node2idx[i]:
        point = node2idx[i]
    flag[i] = True
    for g in G[i]:
        dfs(g)


if not G[1]:
    print(1)
    exit()
dfs(1)
print(point)
