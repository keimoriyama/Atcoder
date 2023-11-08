import heapq

N = int(input())
T, D = [], []
for _ in range(N):
    t, d = map(int, input().split())
    T.append(t)
    D.append((d, d + t))
D.sort()

it, ans = 0, 0
q = []
heapq.heapify(q)
print(D)
for i in range(N):
    print(q, it, i)
    # 印刷機の範囲に印字されていない商品がない
    if len(q) == 0:
        if it == N:
            break
        i = D[it][0]
    while it < N and D[it][0] == i:
        q.append(D[it][1])
        it += 1
    while len(q) > 0 and q[-1] < i:
        q.pop()
    if len(q) > 0:
        q.pop()
        ans += 1

print(ans)
