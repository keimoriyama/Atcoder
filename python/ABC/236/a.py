S = input()
a, b = map(int, input().split())
a -= 1
b -= 1
S_1 = ""
for i, s in enumerate(S):
    if i == a:
        S_1 += S[b]
    elif i == b:
        S_1 += S[a]
    else:
        S_1 += s
print(S_1)
