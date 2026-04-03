S = [input() for _ in range(8)]

r = ["a", "b", "c", "d", "e", "f", "g", "h"]
c = list(reversed([str(i) for i in range(1, 9)]))

for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            p = r[j] + c[i]
            print(p)
