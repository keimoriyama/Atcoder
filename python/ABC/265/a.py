X, Y, N = map(int, input().split())
y = N // 3
x = N - 3 * y
print(min([X * N, x * X + y * Y]))
