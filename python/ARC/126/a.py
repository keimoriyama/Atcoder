T = int(input())

for _ in range(T):
    n2, n3, n4 = map(int, input().split())
    n1, n2, n3 = n2, n4, n3 // 2
    ans = 0
    comb = [(0, 1, 1), (2, 0, 1), (1, 2, 0), (3, 1, 0), (5, 0, 0)]
    for a, b, c in comb:
        k = n1 + n2 + n3
        if a > 0:
            k = min(k, n1 // a)
        if b > 0:
            k = min(k, n2 // b)
        if c > 0:
            k = min(k, n3 // c)
        ans += k
        n1 -= a * k
        n2 -= b * k
        n3 -= c * k

    print(ans)
