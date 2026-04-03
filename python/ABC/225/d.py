N, Q = map(int, input().split())

f = [-1] * (N + 1)
b = [-1] * (N + 1)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, y = q[1], q[2]
        b[x] = y
        f[y] = x
    elif q[0] == 2:
        x, y = q[1], q[2]
        b[x] = -1
        f[y] = -1
    elif q[0] == 3:
        x = q[1]
        ans = []
        while f[x] != -1:
            x = f[x]
        while x != -1:
            ans.append(x)
            x = b[x]
        print(len(ans), end=" ")
        print(*ans)
