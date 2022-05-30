import heapq
from collections import defaultdict
q = int(input())
mx, mn = [], []
cnt = defaultdict(int)
for _ in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        x = query[1]
        cnt[x] += 1
        heapq.heappush(mx, -x)
        heapq.heappush(mn, x)

    if query[0] == 2:
        x,c = query[1:]
        cnt[x] = max(0, cnt[x]-c)

    if query[0] == 3:
        while cnt[-mx[0]] == 0:
            heapq.heappop(mx)
        while cnt[mn[0]] == 0:
            heapq.heappop(mn)
        print(-mx[0]-mn[0])
