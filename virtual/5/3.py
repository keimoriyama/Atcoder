import math
from itertools import combinations

S = []

for _ in range(9):
    S.append(input())

p = []
for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            p.append([i + 1, j + 1])

ans = 0
for p1, p2, p3, p4 in combinations(p, 4):
    l1 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    l2 = (p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2
    l3 = (p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2
    l4 = (p2[0] - p4[0]) ** 2 + (p2[1] - p4[1]) ** 2
    l5 = (p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2
    l6 = (p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2
    l = set([l1, l2, l3, l4, l5, l6])
    if len(l) == 2:
        ans += 1


print(ans)
