N = int(input())
C, P = [], []
for _ in range(N):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)

S_a, S_b = [0] * (N + 1), [0] * (N + 1)
for i in range(1, N + 1):
    c = C[i-1]
    p = P[i-1]
    if c == 1:
        S_a[i] = S_a[i-1] + p
        S_b[i] = S_b[i-1]
    elif c == 2:
        S_b[i] = S_b[i-1] + p
        S_a[i] = S_a[i-1]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    print(S_a[r] - S_a[l], S_b[r] - S_b[l])
