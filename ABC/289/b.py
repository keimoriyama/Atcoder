N, M = map(int, input().split())
a = list(map(int, input().split()))
g = {i + 1: [] for i in range(N)}

for ai in a:
    g[ai].append(ai + 1)
    g[ai + 1].append(ai)


flag = [False] * (N + 1)


def dfs(i):
    route.append(i)
    flag[i] = True
    for gi in g[i]:
        if flag[gi]:
            continue
        return dfs(gi)
    return route


ans = []
for i in range(1, N + 1):
    route = []
    if flag[i]:
        continue
    res = dfs(i)
    ans += list(reversed(res))

print(*ans)
