N = int(input())
a = list(map(int, input().split()))

m = 1
for ai in a:
    m *= ai


def f(m):
    v = 0
    for ai in a:
        v += m % ai
    return v


print(f(m - 1))
