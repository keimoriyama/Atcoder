from functools import cmp_to_key


def cmp(a, b):
    xi, yi, i = a
    xj, yj, j = b
    s = xi * (yj + xj) - xj * (yi + xi)
    return 1 if s > 0 else -1 if s < 0 else 0


N = int(input())
X = []

for i in range(N):
    a, b = map(int, input().split())
    X.append((a, a + b, i))


X.sort(key=cmp_to_key(cmp), reverse=True)

print(*[i + 1 for x, y, i in X])
