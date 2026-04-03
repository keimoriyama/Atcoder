N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(len(A[i])):
        A[i][j] -=1

for i in range(N):
    for j in range(i+1, N):
        A[i].append(A[j][i])

ans = 0
for j in range(N):
    if ans >= j:
        ans = A[ans][j]
    else:
        ans = A[j][ans]
print(ans + 1)
