N, M, K = map(int, input().split())
ans = 0

table = [[0] * (K + 1) for _ in range(N + 1)]
# print(table)
table[0][0] = 1
for i in range(N):
    for j in range(K):
        for k in range(1, M + 1):
            if j + k <= K:
                # print(i + 1, j, k, j + k)
                # print(table[i + 1][j + k])
                table[i + 1][j + k] += table[i][j]

for i in range(K + 1):
    ans += table[-1][i]

print(ans % 998244353)
