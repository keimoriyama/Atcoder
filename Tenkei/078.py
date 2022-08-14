N, M = map(int, input().split())


d = {}
for _ in range(M):
    a, b = map(int, input().split())
    if a not in d.keys():
        d[a] = [b]
    else:
        d[a].append(b)
    if b not in d.keys():
        d[b] = [a]
    else:
        d[b].append(a)

ans = 0
for k in d.keys():
    v = d[k]
    s = sum([1 if value < k else 0 for value in v])
    if s == 1:
        ans += 1

print(ans)
