N = int(input())

s = ""
for i in range(N + 1):
    for ni in range(1, N + 1):
        n = []
        for j in range(1, 10):
            if i % (N / j) == 0:
                n.append(j)
    if len(n) > 0:
        s += str(min(n))
    else:
        s += "-"
print(s)
