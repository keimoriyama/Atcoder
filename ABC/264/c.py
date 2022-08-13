H_1, W_1 = map(int, input().split())
A, B = [], []
for _ in range(H_1):
    A.append(list(map(int, input().split())))

H_2, W_2 = map(int, input().split())

for _ in range(H_2):
    B.append(list(map(int, input().split())))

w, h = [], []
for i in range(1, 2**H_1):
    h = []
    for j in range(H_1):
        if ((i >> j) & 1):
            h.append(j)

    for i in range(1, 2**W_1):
        w = []
        for j in range(W_1):
            if ((i >> j) & 1):
                w.append(j)

        M = []
        for h_1 in h:
            t = []
            a = A[h_1]
            for w_1 in w:
                t.append(a[w_1])
            M.append(t)
        if M == B:
            print("Yes")
            exit()
print("No")
