N = int(input())
table = [[0] * 1001 for _ in range(1001)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    table[lx][ly] += 1
    table[rx][ry] += 1
    table[lx][ry] -= 1
    table[rx][ly] -= 1

for i in range(1001):
    for j in range(1, 1001):
        table[i][j] += table[i][j - 1]
for i in range(1, 1001):
    for j in range(1001):
        table[i][j] += table[i - 1][j]

ans = [0] * (N + 1)

for i in range(1001):
    for j in range(1001):
        if table[i][j] > 0:
            ans[table[i][j]] += 1

for a in ans[1:]:
    print(a)
