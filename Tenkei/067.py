def base8_to_10(N):
    a = 0
    for i, n in enumerate(reversed(N)):
        a += int(n) * 8**i
    return a


def base10_to_9(N):
    res = ""
    while N > 0:
        n = N % 9
        res = str(n) + res
        N = N // 9
    return res


N, K = map(int, input().split())

if N == 0:
    print(0)
    exit()
for _ in range(K):
    N = base10_to_9(base8_to_10(str(N)))
    N = N.replace("8", "5")

print(N)
