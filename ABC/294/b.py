from string import ascii_uppercase

c = list(ascii_uppercase)
H, W = map(int,input().split())

A = []
for _ in range(H):
    A.append(list(map(int,input().split())))


for i in range(H):
    for j in range(W):
        if A[i][j] == 0:
            print(".", end = "")
        else:
            print(c[A[i][j]-1], end ="")

    print()
