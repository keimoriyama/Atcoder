from collections import defaultdict

N = int(input())
sc = defaultdict(int)
flag = {k: False for k in sc.keys()}
for _ in range(N):
    n, c = map(int, input().split())
    sc[n] = c

k = list(sc.keys())
k_set = set(k)
for si in k:
    base_c = sc[si]
    ci = sc[si]
    next_si = si
    n = 0
    while ci > 1:
        ci //= 2
        next_si *= 2
    sc[next_si] = ci
    sc[si] = ci

print(sc)
ans = 0
for ci in sc.values():
    ans += ci
print(ans)
