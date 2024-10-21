from copy import deepcopy

N = int(input())

A = [list(input()) for _ in range(N)]
ans = deepcopy(A)


for i in range(N):
    for j in range(N):
        d = min(i+1, j+1, N-i, N-j)
        ni = i
        nj = j
        for _ in range(d%4):
            ti = nj
            tj = N - 1 - ni
            ni = ti
            nj = tj
        ans[ni][nj] = A[i][j]

for i in range(N):
    for j in range(N):
        print(ans[i][j], end="")
    print()
