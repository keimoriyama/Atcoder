from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


def f(x, y):
    return x * W + y


H, W = map(int, input().split())
Q = int(input())
d = [[0] * (W + 1) for _ in range(H + 1)]
tree = UnionFind((H + 1) * (W + 1))
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c = q[1] - 1, q[2] - 1
        d[r][c] = 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 or j == 0):
                    continue
                a = r + i
                b = c + j
                if 0 <= a < H and 0 <= b < W and d[a][b] == 1:
                    tree.union(f(a, b), f(r, c))
    if q[0] == 2:
        ra, ca, rb, cb = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
        if d[ra][ca] == 1 and d[rb][cb] == 1 and tree.same(f(ra, ca), f(rb, cb)):
            print("Yes")
        else:
            print("No")
