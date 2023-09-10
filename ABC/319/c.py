from itertools import permutations

c = []
for _ in range(3):
    c += list(map(int, input().split()))

row = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

order = [i for i in range(10)]

n = 0
total = 0
for o in permutations(order):
    dis = False
    total += 1
    for x, y, z in row:
        if c[x] == c[y] and o[x] < o[z] and o[y] < o[z]:
            dis = True
        elif c[x] == c[z] and o[x] < o[y] and o[z] < o[y]:
            dis = True
        elif c[y] == c[z] and o[y] < o[x] and o[z] < o[x]:
            dis = True
    if not dis:
        n += 1

print(n / total)
