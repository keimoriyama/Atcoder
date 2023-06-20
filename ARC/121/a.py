from itertools import combinations

N = int(input())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))

X_sort = sorted(X)
Y_sort = sorted(Y)

l = []
for i in range(2):
    l += [X_sort[i][1], X_sort[-i - 1][1], Y_sort[i][1], Y_sort[-i - 1][1]]

l = list(set(l))
d = []

for v1, v2 in combinations(l, 2):
    dis = max(abs(X[v1][0] - X[v2][0]), abs(Y[v1][0] - Y[v2][0]))
    d.append(dis)

if len(d) == 1:
    print(d[0])
else:
    print(sorted(d)[-2])
