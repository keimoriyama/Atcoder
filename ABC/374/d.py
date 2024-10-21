from itertools import permutations
from math import sqrt

def calc_dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


N, S, T = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(N)]
ans = 10**100
lines = list(range(N))
for order in permutations(lines, N):
    for i in range(2**N):
        m = [(i >> j) & 1 for j in range(N)]
        tmp = 0
        s = [0, 0]
        for oi in order:
            if m[oi] == 0:
                g = [ABCD[oi][0], ABCD[oi][1]]
            else:
                g = [ABCD[oi][2], ABCD[oi][3]]
            tmp += calc_dist(s[0], s[1], g[0], g[1]) / S
            tmp += calc_dist(ABCD[oi][0], ABCD[oi][1], ABCD[oi][2], ABCD[oi][3]) / T
            if m[oi] == 0:
                s = [ABCD[oi][2], ABCD[oi][3]]
            else:
                s = [ABCD[oi][0], ABCD[oi][1]]
        ans = min(ans, tmp)

print(ans)
