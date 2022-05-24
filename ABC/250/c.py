N, Q = map(int, input().split())
a = [i for i in range(1, N+1)]
index = [i for i in range(1, N+1)]
X = []

for _ in range(Q):
    X.append(int(input()))

for x in X:
    p1 = index[x]
    p2 = p1
    if p1 != N:
        p1 += 1
    else:
        p1 -= 1
    print(x, p1, p2, N)
    v1 = a[p1]
    v2 = a[p2]
    a[p1] , a[p2] = a[p2], a[p1]
    index[v1] ,index[v2] = index[v2] ,index[v1]

a = [str(i) for i in a]
print(" ".join(a))
