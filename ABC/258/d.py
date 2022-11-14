N, X = map(int, input().split())

init = 0
min_t = 0
for i in range(N):
    a, b = map(int, input().split())
    init = init + a + b
    if i == 0:
        min_t = init + b * (X - i - 1)
    elif init > -min_t:
        break
    else:
        min_t = min(min_t, init + b * (X - i - 1))

print(min_t)
