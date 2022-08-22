from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cr, cnt = 0, 0
map = defaultdict(int)
ans = -1
for i in range(N):
    while cr < N:
        if cnt == K and map[A[cr]] == 0:
            break
        if map[A[cr]] == 0:
            cnt += 1
        map[A[cr]] += 1
        cr += 1
    ans = max(ans, cr - i)
    if map[A[i]] == 1:
        cnt -= 1
    map[A[i]] -= 1

print(ans)
