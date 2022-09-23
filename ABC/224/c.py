N = int(input())
p = []
for _ in range(N):
    x, y = map(int, input().split())
    p.append([x, y])

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            x1, y1 = p[i][0], p[i][1]
            x2, y2 = p[j][0], p[j][1]
            x3, y3 = p[k][0], p[k][1]
            if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) != 0:
                ans += 1

print(ans)
