H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
x, y = [], []
for i, s in enumerate(S):
    for j, t in enumerate(s):
        if t == "-":
            continue
        elif t == "o":
            x.append(i)
            y.append(j)

print(abs(x[0]-x[1]) + abs(y[0]-y[1]))
