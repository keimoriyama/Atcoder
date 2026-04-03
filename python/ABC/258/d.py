n, x = map(int, input().split())
init_time = 0
min_time = 0
for i in range(n):
    a, b = map(int, input().split())

    init_time = init_time + a + b
    if i == 0:
        min_time = init_time + b * (x - i - 1)
    elif init_time >= min_time:
        break
    else:
        min_time = min(min_time, init_time + b * (x - i - 1))

print(min_time)
