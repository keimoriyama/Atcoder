N = int(input())


for i in range(N, 1000):
    n = i // 100
    m = i // 10 % 10
    h = int(str(i)[-1])
    # print(n, m, h)
    if n * m == h:
        print(i)
        exit()
