N, K = map(int, input().split())

P = []
for _ in range(N):
    P.append(list(map(int, input().split())))

t = [[sum(p), i] for i, p in enumerate(P)]


base = sorted(t, reverse=True)[K - 1]
for t_i in t:
    if t_i[0] + 300 >= base[0]:
        print("Yes")
    else:
        print("No")
