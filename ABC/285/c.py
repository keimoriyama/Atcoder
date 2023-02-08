from string import ascii_uppercase

S = input()

converter = {a: i + 1 for i, a in enumerate(list(ascii_uppercase))}

ans = 0
for i in range(1, len(S) + 1):
    n = converter[S[len(S) - i]]
    ans += n * 26 ** (i - 1)

print(ans)
