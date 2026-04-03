N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

q = []
q.append(1)
cnt = [0] * (N + 1)
dist = [-1] * (N + 1)
dist[1] = 0
cnt[1] = 1
for v in q:
    for vv in G[v]:
        if dist[vv] == -1:
            dist[vv] = dist[v] + 1
            q.append(vv)
            cnt[vv] = cnt[v]
        elif dist[vv] == dist[v] + 1:
            cnt[vv] += cnt[v]
print(cnt[N] % (10**9 + 7))
