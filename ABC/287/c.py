N, M = map(int, input().split())
G = {i: [] for i in range(N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

if M != N - 1:
    print("No")
    exit()

for i in range(1, N + 1):
    if len(G[i]) > 2:
        print("No")
        exit()

reach = [False] * (N + 1)
que = []
que.append(1)
reach[1] = True
while que:
    u = que.pop(0)
    for v in G[u]:
        if reach[v]:
            continue
        reach[v] = True
        que.append(v)

for r in reach[1:]:
    if not r:
        print("No")
        exit()

print("Yes")
