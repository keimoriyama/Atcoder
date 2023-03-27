S = list(input())
S = [0] + S
for i in range(1, len(S) // 2 + 1):
    S[2 * i], S[2 * i - 1] = S[2 * i - 1], S[2 * i]

print("".join(map(str, S[1:])))
