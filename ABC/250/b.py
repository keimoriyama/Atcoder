N, A, B = map(int, input().split())
S = [[0] * N * B for i in range(A*N)]
for i in range(N * A):
    for j in range(N * B):
        if (int(i/A)+int(j/B)) % 2 == 0:
            S[i][j] = "."
        else:
            S[i][j] = "#"

for i in range(len(S)):
    for j in range(len(S[i])):
        print(S[i][j], end="")
    print()
