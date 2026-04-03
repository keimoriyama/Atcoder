from collections import deque

n, m = map(int, input().split())
g = {i: [] for i in range(n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

flag = [False] * (n + 1)
s = 0
for i in range(1, n + 1):
    if flag[i]:
        continue
    s += 1
    q = deque()
    q.append(i)
    while q:
        v = q.popleft()
        for gi in g[v]:
            if flag[gi]:
                continue
            flag[gi] = True
            q.append(gi)

print(m - n + s)
