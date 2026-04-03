from collections import deque

N, M = map(int, input().split())
L = [[] for _ in range(N)]


for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    L[u].append(v)
    L[v].append(u)

f = [False] * N

for i in range(N):
    if f[i]:
        continue
    q = deque()
    q.append(i)
    e, v, loop = 0, 0, 0
    while q:
        n = q.popleft()
        v += 1
        f[n] = True
        for l in L[n]:
            e += 1
            if not f[l]:
                f[l] = True
                q.append(l)
    if e // 2 + loop != v:
        print("No")
        exit()

print("Yes")
