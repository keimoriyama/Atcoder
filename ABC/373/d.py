N, M = map(int,input().split())
uvw = [list(map(int,input().split())) for _ in range(M)]
G = {i+1: [] for i in range(N)}
W = {}
for uvwi in uvw:
    u, v, w = uvwi
    G[u].append(v)
    G[v].append(u)
    W[(u,v)] = w
    W[(v,u)] = -w

visited = [False] * (N+ 1)
ans = [0] * (N+1)
for i in range(1,N+1):
    if visited[i]:
        continue
    st = [i]
    visited[i] = True
    while st:
        u = st.pop()
        for v in G[u]:
            if visited[v]:
                continue
            visited[v] = True
            ans[v] = ans[u] + W[(u,v)]
            st.append(v)

print(*ans[1:])
