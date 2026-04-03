N = int(input())
K = list(map(int,input().split()))

A, B = 0, 0
ans = 10**100
for i in range(2 ** N):
    tmp_A, tmp_B = 0, 0
    for j in range(N):
        if ((i >> j) & 1):
            tmp_A += K[j]
        else:
            tmp_B += K[j]
    ans = min(ans, max(tmp_A, tmp_B))

print(ans)
