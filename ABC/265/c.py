H, W = map(int, input().split())
G = []
for _ in range(H):
    G.append(input())
F = [[0] * W for _ in range(H)]

i, j = 0, 0
prev_pos = [[i, j]]
while True:
    if F[i][j] == 1:
        if prev_pos[-1] == prev_pos[-2]:
            break
        print(-1)
        exit()
    F[i][j] = 1
    if G[i][j] == "U" and i != 0:
        i -= 1
    elif G[i][j] == "D" and i != H - 1:
        i += 1
    elif G[i][j] == "L" and j != 0:
        j -= 1
    elif G[i][j] == "R" and j != W - 1:
        j += 1
    prev_pos.append([i, j])

print(i + 1, j + 1)
