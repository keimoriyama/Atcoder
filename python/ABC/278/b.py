H, M = map(int, input().split())

for i in range(24 * 60):
    A = H // 10
    B = H % 10
    C = M // 10
    D = M % 10
    H1 = A * 10 + C
    M1 = B * 10 + D
    if 0 <= H1 < 24 and 0 <= M1 < 60:
        print(H, M)
        exit()

    M += 1
    if M == 60:
        M = 0
        H += 1
    if H == 24:
        H = 0
