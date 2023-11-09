import heapq

N = int(input())
D = []
for _ in range(N):
    t, d = map(int, input().split())
    D.append([t, d + t])
D.sort()

it, ans = 0, 0
que = []
heapq.heapify(que)
t = 0
idx = 0
ans = 0
while idx < N or que:
    while idx < N and D[idx][0] <= t:
        heapq.heappush(que, D[idx][1])
        idx += 1
    while que and que[0] < t:
        heapq.heappop(que)

    if que:
        ans += 1
        heapq.heappop(que)
    if not que and idx < N:
        t = D[idx][0]
    else:
        t += 1

print(ans)
