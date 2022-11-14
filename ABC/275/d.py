from math import floor
import sys
from functools import lru_cache

sys.setrecursionlimit(2000000)

N = int(input())


@lru_cache
def f(x):
    if x == 0:
        return 1
    return f(floor(x / 2)) + f(floor(x / 3))


print(f(N))
