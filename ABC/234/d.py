import heapq

N, K = map(int, input().split())
P = list(map(int, input().split()))

p = P[:K]
print(min(p))
heapq.heapify(p)
for i in range(K, N):
    minima = heapq.heappop(p)
    minima = max(minima, P[i])
    heapq.heappush(p, minima)
    ans = heapq.heappop(p)
    print(ans)
    heapq.heappush(p, ans)
