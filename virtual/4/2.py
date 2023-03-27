from math import floor

A, B, N = map(int, input().split())


def f(x):
    return floor(A * x / B) - A * floor(x / B)


print(f(min(B - 1, N)))
