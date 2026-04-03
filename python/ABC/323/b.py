N = int(input())
S = [input() for _ in range(N)]

wins = []
for i in range(N):
    win_i = 0
    for j in range(N):
        if S[j][i] == "-":
            continue
        if S[j][i] == "o":
            win_i += 1
    wins.append((win_i, i + 1))

for s in sorted(wins):
    print(s[1], end=" ")
print()
