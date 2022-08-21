N = int(input())
S = input()
D = [[0] * (len(S) + 1) for _ in range(8)]
D[0][0] = 1
for i in range(1, len(S)):
    for j in range(1, 8):
        D[i + 1][j] += D[i][j]
        if S[i] == "a" and j == 0:
            D[i + 1][j + 1] += D[i][j]
        if S[i] == "t" and j == 1:
            D[i + 1][j + 1] += D[i][j]
        if S[i] == "c" and j == 2:
            D[i + 1][j + 1] += D[i][j]
        if S[i] == "o" and j == 3:
            D[i + 1][j + 1] += D[i][j]
        if S[i] == "r" and j == 4:
            D[i + 1][j + 1] += D[i][j]
        if S[i] == "d" and j == 5:
            D[i + 1][j + 1] += D[i][j]
        if S[i] == "e" and j == 6:
            D[i + 1][j + 1] += D[i][j]
        if S[i] == "r" and j == 7:
            D[i + 1][j + 1] += D[i][j]
        print(i, j, D[i + 1][j])
    for j in range(8):
        D[i + 1][j] %= 1000000007
print(D[-1][-1])
