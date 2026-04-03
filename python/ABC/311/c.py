import sys

sys.setrecursionlimit(200000000)
N = int(input())

G = {i: -1 for i in range(1, N + 1)}
A = list(map(int, input().split()))
for i, a in enumerate(A):
    G[i + 1] = a

flag = [False] * (N + 1)


add = True


def dfs(i):
    global add
    flag[i] = True
    if G[i] == -1:
        return None, None
    if flag[G[i]]:
        return [i], G[i]
    else:
        res, last = dfs(G[i])
        if res is None:
            return None
        else:
            if add:
                res.append(i)
            if i == last:
                add = False
            return res, last


for i in range(1, N + 1):
    if flag[i]:
        continue
    res, _ = dfs(i)

    if res is not None:
        print(len(res))
        print(*list(reversed(res)))
        exit()
