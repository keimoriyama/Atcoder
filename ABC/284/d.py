from math import sqrt


T = int(input())
for _ in range(T):
    N = int(input())
    for n in range(2, N):
        if N % n == 0:
            break
    if N % (n**2) == 0:
        p, q = n, N // (n**2)
    else:
        p, q = round((N / n) ** 0.5), n
    print(p, q)
