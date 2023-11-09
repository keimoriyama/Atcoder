P1 = [list(input()) for _ in range(4)]
P2 = [list(input()) for _ in range(4)]
P3 = [list(input()) for _ in range(4)]


def rotate(l):
    w = l
    for i in range(4):
        for j in range(4):
            l[i][j] = w[3 - j][i]

    return l


for p in P1:
    print(p)
for p in rotate(P1):
    print(p)
