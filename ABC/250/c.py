N, Q = map(int, input().split())
a = [i for i in range(N+1)]
index = [i for i in range(N+1)]
X = []

for _ in range(Q):
    X.append(int(input()))

for x in X:
    p1 = index[x]
    p2 = p1
    if p1 != N: p2 += 1
    else: p2 -= 1
    v1 = a[p1]
    v2 = a[p2]
    a[p1] , a[p2] = a[p2], a[p1]
    index[v1] ,index[v2] = index[v2] ,index[v1]

a = [str(i) for i in a[1:]]
print(" ".join(a))
