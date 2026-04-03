class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.L = list(range(n))
        self.R = list(range(n))
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.L[x] = min(self.L[x], self.L[y])
        self.R[x] = max(self.R[x], self.R[y])
        self.parents[y] = x
    def get_LR(self, x):
        x = self.find(x)
        return (self.L[x], self.R[x])
H, W, Q = map(int, input().split())
uf_row = [UnionFind(W + 2) for i in range(H + 2)]
uf_col = [UnionFind(H + 2) for i in range(W + 2)]
erased = [[0] * (W + 2) for i in range(H + 2)]
ans = H * W
def erase(x, y):
    global ans
    if 1 <= x <= H and 1 <= y <= W:
        ans -= 1
        erased[x][y] = 1
        if erased[x][y - 1]:
            uf_row[x].merge(y - 1, y)
        if erased[x][y + 1]:
            uf_row[x].merge(y, y + 1)
        if erased[x - 1][y]:
            uf_col[y].merge(x - 1, x)
        if erased[x + 1][y]:
            uf_col[y].merge(x, x + 1)
ans = H * W
for _ in range(Q):
    x, y = map(int, input().split())
    if erased[x][y] == 0:
        erase(x, y)
        continue
    Lx, Rx = uf_col[y].get_LR(x)
    Ly, Ry = uf_row[x].get_LR(y)
    erase(Lx - 1, y)
    erase(Rx + 1, y)
    erase(x, Ly - 1)
    erase(x, Ry + 1)
print(ans)
