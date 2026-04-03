N = int(input())
S = []
for i in range(N):
    S.append(input())

C = [[0] * 10 for _ in range(10)]

for i in range(N):
    for j in range(10):
        C[int(S[i][j])][j] += 1

res = []
for i in range(10):
    num = N
    t = 0
    while num != 0:
        if C[i][t % 10] > 0:
            C[i][t % 10] -= 1
            num -= 1
        t += 1
    res.append(t) 

print(min(res) - 1)
