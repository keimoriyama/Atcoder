def f(N):
    if N == 0:
        return 1
    else:
        return N * f(N - 1)


print(f(int(input())))
