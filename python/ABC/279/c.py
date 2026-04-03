H, W = map(int, input().split())
S = [input() for _ in range(H)]
T = [input() for _ in range(H)]

s_t, t_t = [], []
for i in range(W):
    t_a, t_b = [], []
    for j in range(H):
        s = S[j][i]
        t = T[j][i]
        t_a.append(s)
        t_b.append(t)
    s_t.append(tuple(t_a))
    t_t.append(tuple(t_b))

s_t = sorted(s_t)
t_t = sorted(t_t)

if all([a == b for a, b in zip(s_t, t_t)]):
    print("Yes")
else:
    print("No")
