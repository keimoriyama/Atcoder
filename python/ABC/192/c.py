def g1(x):
    x = sorted(x)
    x = int("".join(x))
    return x


def g2(x):
    x = sorted(x, reverse=True)
    x = int("".join(x))
    return x


def f(x):
    x = [i for i in str(x)]
    return g2(x) - g1(x)


N, K = map(int, input().split())

a = N
for i in range(K):
    a = f(a)

print(a)
