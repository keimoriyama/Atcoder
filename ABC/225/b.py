N = int(input())
G = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N + 1):
    G[i].append(i)

for g in G:
    if len(g) == N:
        print("Yes")
        exit()


print("No")
