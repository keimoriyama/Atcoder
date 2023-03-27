W, H, N = map(int, input().split())

x_max, x_min, y_max, y_min = W, 0, H, 0
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        x_min = max(x_min, x)
    elif a == 2:
        x_max = min(x_max, x)
    elif a == 3:
        y_min = max(y_min, y)
    else:
        y_max = min(y_max, y)
# print(x_min, x_max, y_min, y_max)
if x_min > x_max or y_min > y_max:
    print(0)
else:
    print((x_max - x_min) * (y_max - y_min))
