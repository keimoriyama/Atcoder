N, M = map(int, input().split())
A = [input() for _ in range(2 * N)]


def judge(a, b):
    if a == b:
        return -1
    if a == "G" and b == "P":
        return 1
    if a == "C" and b == "G":
        return 1
    if a == "P" and b == "C":
        return 1
    return 0


rank = [[0, i] for i in range(2 * N)]

for j in range(M):
    for i in range(N):
        p1 = rank[2 * i][1]
        p2 = rank[2 * i + 1][1]
        res = judge(A[p1][j], A[p2][j])
        if res != -1:
            rank[2 * i + res][0] -= 1
    rank.sort()

for _, i in rank:
    print(i + 1)
