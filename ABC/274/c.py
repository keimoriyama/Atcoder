N = int(input())
A = list(map(int, input().split()))
tree = {i + 1: -1 for i in range(2 * len(A) + 1)}
d = {i + 1: -1 for i in range(2 * len(A) + 1)}
tree[1] = 0
d[1] = 0
for i, a in enumerate(A):
    i += 1
    tree[2 * i] = a
    tree[2 * i + 1] = a
    d[2 * i] = d[a] + 1
    d[2 * i + 1] = d[a] + 1

for i in d.values():
    print(i)
