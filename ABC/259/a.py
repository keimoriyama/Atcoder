N, M, X, T, D = map(int, input().split())

if X <= M:
    print(T)
else:
    diff = (X - M) * D
    print(T - diff)