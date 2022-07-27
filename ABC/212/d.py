import heapq
q = int(input())

balls = []
heapq.heapify(balls)
diff = 0
for i in range(q):
    q = list(map(int, input().split()))
    op = q[0]
    if op == 1:
        x = q[1]
        heapq.heappush(balls, x - diff)
    elif op == 2:
        x = q[1]
        diff += x
    else:
        n = heapq.heappop(balls)
        print(n + diff)
