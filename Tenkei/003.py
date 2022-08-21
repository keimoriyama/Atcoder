def get_dist(start):
    # BFSで距離を計算する
    global N, D
    d = [1e9] * (N + 1)
    q = [start]
    d[start] = 0
    while len(q) > 0:
        p = q.pop(0)
        for t in D[p]:
            if d[t] == 1e9:
                d[t] = d[p] + 1
                q.append(t)
    return d


N = int(input())
D = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    D[a].append(b)
    D[b].append(a)

dist = get_dist(1)

max_n = -1
max_i = 0
for i in range(1, N + 1):
    if max_n < dist[i]:
        max_n = dist[i]
        max_i = i

dist_max = get_dist(max_i)
max2 = -1
for i in range(1, N + 1):
    max2 = max(max2, dist_max[i])
print(max2 + 1)
