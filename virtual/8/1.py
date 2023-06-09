N = int(input())
S = [input() for _ in range(N)]


def lcp(x, y):
    n = min(len(x), len(y))
    c = 0
    for k in range(n):
        if x[k] == y[k]:
            c += 1
        else:
            break
    return c


for i in range(N):
    ans = 0
    for j in range(N):
        if i == j:
            continue
        ans = max(ans, lcp(S[i], S[j]))
    print(ans)
