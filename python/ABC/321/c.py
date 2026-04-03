K = int(input())
ns = []
for i in range(2, 2**10):
    n1 = 0
    for j in reversed(range(10)):
        if i & (1 << j):
            n1 *= 10
            n1 += j
    ns.append(n1)
ns.sort()
print(ns[K - 1])
