N = int(input())

S = []
for _ in range(N):
    S.append(input())

d = {}
for s in S:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

print(max(d, key=d.get))
