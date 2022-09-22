S = []
for _ in range(10):
    S.append(input())

x, y = [], []
for i in range(10):
    for j in range(10):
        if S[i][j] == "#":
            x.append(i)
            y.append(j)

print(min(x) + 1, max(x) + 1)
print(min(y) + 1, max(y) + 1)
