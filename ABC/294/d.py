from heapq import heapify, heappop, heappush

N, Q = map(int, input().split())

called = []
wait = set()
heapify(called)
idx, min_v = 1, 1
ans = []
for _ in range(Q):
    e = input().split()
    if e[0] == "1":
        heappush(called, idx)
        idx += 1
    elif e[0] == "2":
        call = int(e[1])
        wait.add(call)
    else:
        while called:
            if called[0] in wait:
                wait.discard(called[0])
                heappop(called)
            else:
                print(called[0])
                break
