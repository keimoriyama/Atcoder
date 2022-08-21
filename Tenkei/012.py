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


H, W = map(int, input().split())
Q = int(input())
d = [[0] * (W + 1) for _ in range(H + 1)]
tree = UnionFind((H + 1) * (W + 1))
for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        r, c = int(q[1]), int(q[2])
        d[r][c] = 1
        if r - 1 > 0 and d[r - 1][c] == 1:
            tree.union((r - 1) * c, r * c)
        if r + 1 <= H and d[r + 1][c] == 1:
            tree.union((r + 1) * c, r * c)
        if c - 1 > 0 and d[r][c - 1] == 1:
            tree.union((c - 1) * r, r * c)
        if c + 1 <= W and d[r][c + 1] == 1:
            tree.union((c + 1) * r, r * c)
    elif q[0] == "2":
        rai, cai, rbi, cbi = int(q[1]), int(q[2]), int(q[3]), int(q[4])
        if d[rai][cai] == 0 or d[rbi][cbi] == 0:
            print("No")
        elif tree.same(rai * cai, rbi * cbi):
            print("Yes")
        else:
            print("No")
