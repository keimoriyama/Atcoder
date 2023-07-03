from math import gcd

L, R = map(int, input().split())


def calc(l, r):
    print(l, r)
    if gcd(l, r) == 1:
        return r - l
    else:
        return max(calc(l + 1, r), calc(l, r - 1))


print(calc(L, R))
