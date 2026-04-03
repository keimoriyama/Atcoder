A, B = map(int, input().split())


def f(n):
    return B * n + A / ((n + 1) ** 0.5)


ans = f(0)

p = ((A / (2 * B)) ** 2) ** (1 / 3)
p = int(p)

for i in range(-10, 10):
    n = i + p
    if n < 0:
        continue
    ans = min(ans, f(n))

print(ans)
