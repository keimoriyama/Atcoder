N, M = map(int, input().split())
K, X = [], []
for _ in range(M):
    i = list(map(int, input().split()))
    K.append(i[0])
    X.append(i[1:])

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        a = 0
        for x in X:
            if (i in x) and (j in x):
                a += 1
        if a == 0:
            print("No")
            exit()


print("Yes")
