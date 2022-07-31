N, X, Y = map(int, input().split())

r = [0] * 12
b = [0] * 12
b[1] = 1
for i in range(2, N+1):
    b[i] = r[i-1] + b[i-1] * Y
    r[i] = r[i-1] + b[i] * X

print(r[N])