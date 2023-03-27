W, H, N = map(int, input().split())
xmax, xmin, ymax, ymin = 0, W, 0, H
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        xmax = max(xmax, x)
    elif a == 2:
        xmin = min(xmin, x)
    elif a == 3:
        ymax = max(ymax, y)
    else:
        ymin = min(ymin, y)

ans = (xmin - xmax) * (ymin - ymax)
if ans > 0 and (xmin - xmax) > 0 and (ymin - ymax) > 0:
    print(ans)
else:
    print(0)
