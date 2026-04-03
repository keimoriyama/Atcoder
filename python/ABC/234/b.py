import math

N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

max = 0
for i in range(N):
    for j in range(i + 1, N):
        x_1, y_1 = X[i], Y[i]
        x_2, y_2 = X[j], Y[j]
        diff = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2
        if max < diff:
            max = diff

print(math.sqrt(max))
