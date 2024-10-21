from math import sqrt

N = int(input())
prev_x, prev_y = 0, 0

ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    ans += dist
    prev_x, prev_y = x, y

ans += sqrt(prev_x**2 + prev_y**2)
print(ans)
