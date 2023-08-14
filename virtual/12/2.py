import bisect

N = int(input())
D = sorted(list(map(int, input().split())))
M = int(input())
T = sorted(list(map(int, input().split())))

d = {i: 0 for i in D}
for di in D:
    d[di] += 1

t = {i: 0 for i in T}
for ti in T:
    t[ti] += 1

for t in T:
    l, r = 0, N - 1
    ok = False
    while l <= r:
        m = (l + r) // 2
        if D[m] == t:
            ok = True
            break
        elif D[m] < t:
            l = m + 1
        else:
            r = m - 1
    if ok:
        if d[t] > 0:
            d[t] -= 1
        else:
            print("NO")
            exit()
    else:
        print("NO")
        exit()


print("YES")
