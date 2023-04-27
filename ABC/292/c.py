import math

N = int(input())

ans = 0

for i in range(N):
    X, Y = i, N - i
    x, y = 0, 0
    for j in range(1, int(math.sqrt(X)) + 1):
        if X % j == 0:
            x += 1
            if X != j * j:
                x += 1
    for j in range(1, int(math.sqrt(Y)) + 1):
        if Y % j == 0:
            y += 1
            if Y != j * j:
                y += 1
    ans += x * y

print(ans)
