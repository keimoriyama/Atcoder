H, W = map(int, input().split())
C = []
for _ in range(H):
    C.append(input())

for i in range(W):
    n = 0
    for j in range(H):
        if C[j][i] == "#":
            n += 1
    print(n, end=" ")
