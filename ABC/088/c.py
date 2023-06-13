c = [list(map(int, input().split())) for _ in range(3)]

for a1 in range(-100, 100):
    for a2 in range(-100, 100):
        for a3 in range(-100, 100):
            b1 = c[0][0] - a1
            b2 = c[0][1] - a1
            b3 = c[0][2] - a1
            A = [a1, a2, a3]
            B = [b1, b2, b3]
            ok = True
            for i in range(3):
                for j in range(3):
                    if c[i][j] != A[i] + B[j]:
                        ok = False
            # print(A, B)
            if ok:
                print("Yes")
                exit()


print("No")
