from collections import defaultdict

N = int(input())
p = []
p_exist = defaultdict(int)
for _ in range(N):
    x, y = map(int, input().split())
    p.append([x, y])
    p_exist[(x, y)] = 1

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = p[i]
        x2, y2 = p[j]
        if x1 == x2 or y1 == y2:
            continue

        if p_exist[(x1, y2)] == 1 and p_exist[(x2, y1)] == 1:
            ans += 1
ans //= 2
print(ans)
