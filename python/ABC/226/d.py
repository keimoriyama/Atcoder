from math import atan2

N = int(input())
p = []
for _ in range(N):
    x, y = map(int, input().split())
    p.append((x, y))

ans = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        pi, pj = p[i], p[j]
        a = pi[0] - pj[0]
        b = pi[1] - pj[1]
        for k in [1, -1]:
            theta = atan2(b, a)
            # print(theta, a, b)
            ans.add(theta)


print(len(ans))
