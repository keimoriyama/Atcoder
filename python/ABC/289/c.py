N, M = map(int, input().split())
A = []
for _ in range(M):
    c = input()
    a = set(list(map(int, input().split())))
    A.append(a)
# print(A)
ans = 0
for i in range(2**M):
    s = set()
    for j in range(M):
        if (i >> j) & 1:
            s |= A[j]
    # print(s)
    f = True
    for i in range(1, N + 1):
        if i not in s:
            f = False
            break
    if f:
        ans += 1
print(ans)

"""
d = {i + 1: [] for i in range(N)}

for i, a in enumerate(A):
    for j in range(1, N + 1):
        if j not in a:
            continue
        d[j].append(i)

print(A)
print(d)
"""
