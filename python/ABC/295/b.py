R, C = map(int, input().split())
B = []
for _ in range(R):
    B.append(list(input()))

P = []
for i in range(R):
    for j in range(C):
        if B[i][j] == ".":
            P.append([i, j])
map = [[False] * C for _ in range(R)]
for p in P:
    map[p[0]][p[1]] = True

for i in range(R):
    for j in range(C):
        if B[i][j] == "#" or B[i][j] == ".":
            continue
        r = int(B[i][j])
        for k in range(R):
            for l in range(C):
                if abs(i - k) + abs(j - l) <= r:
                    map[k][l] = True

for i in range(R):
    for j in range(C):
        if map[i][j]:
            print(".", end="")
        else:
            print("#", end="")
    print()
