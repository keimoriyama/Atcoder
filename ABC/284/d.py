from math import sqrt, pow


T = int(input())
for _ in range(T):
    N = int(input())
    p, q = 0, 0
    f = False
    i = 2
    while i**3 <= N:
        if N % i != 0:
            i += 1
            continue
        if (N / i) % i == 0:
            p = i
            q = N / i / i
        else:
            q = i
            p = int(sqrt(N / i))
        break
    print(int(p), int(q))
