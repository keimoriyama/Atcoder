N, Q = map(int, input().split())

ff_pair = set()
for _ in range(Q):
    t, a, b = map(int, input().split())
    p1 = (a, b)
    p2 = (b, a)
    if t == 1:
        ff_pair.add(p1)
    elif t == 2:
        if p1 in ff_pair:
            ff_pair.remove(p1)
    elif t == 3:
        if p1 in ff_pair and p2 in ff_pair:
            print("Yes")
        else:
            print("No")
