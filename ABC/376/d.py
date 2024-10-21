from collections import deque

N, M = map(int, input().split())
G = {i: [] for i in range(N)}

for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)


inf = 10**9
f = [inf] * N
q = deque()
q.append(0)
f[0] = 0

while q:
    p = q.popleft()
    for n_p in G[p]:
        if n_p == 0:
            print(f[p] + 1)
            exit()
        if f[n_p] == inf:
            f[n_p] = f[p] + 1
            q.append(n_p)

print(-1)


