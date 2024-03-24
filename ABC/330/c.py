from math import sqrt

D = int(input())

lim = int(sqrt(D)) + 1
ans = 1e100
for x in range(lim):
    if x ^ 2 - D >= 0:
        ans = min(ans, x ^ 2 - D)

print(ans)
