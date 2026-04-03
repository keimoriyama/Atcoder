N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

ans = 0
j = 0
for i in range(N):
    if j == M:
        break
    if A[i] < B[j]:
        continue
    ans += A[i]
    j += 1

if j == M:
    print(-1 if ans == 0 else ans)
else:
    print(-1)
