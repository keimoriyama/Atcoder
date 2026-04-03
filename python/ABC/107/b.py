H, W = map(int, input().split())
a = [input() for _ in range(H)]

col = []
for i in range(H):
    ok = True
    for j in range(W):
        if a[i][j] == "#":
            ok = False
    if ok:
        col.append(i)

row = []
for j in range(W):
    ok = True
    for i in range(H):
        if a[i][j] == "#":
            ok = False
    if ok:
        row.append(j)

for i in range(H):
    if i in col:
        continue
    for j in range(W):
        if j in row:
            continue
        else:
            print(a[i][j], end="")
    print()
