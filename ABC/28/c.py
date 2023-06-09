N = list(map(int, input().split()))
se = set()
for i in range(2 ** len(N)):
    n = 0
    su = 0
    for j in range(len(N)):
        if i & (1 << j):
            n += 1
            su += N[j]
    if n == 3:
        se.add(su)

print(sorted(list(se))[-3])
