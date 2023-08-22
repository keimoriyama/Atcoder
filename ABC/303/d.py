X, Y, Z = map(int, input().split())
S = input()

caps = False
tokens = [[S[0], 1]]
for s in S[1:]:
    if tokens[-1][0] != s:
        tokens.append([s, 1])
    else:
        tokens[-1][1] += 1

print(tokens)
ans = 0
cap_tok = "x"
for tok in tokens:
    t = tok[0]
    n = int(tok[1])
    if cap_tok != t:
        if X * n + Z < Y * n:
            ans += X * n + Z
            caps = True
            cap_tok = t
        else:
            ans += Y * n
    else:
        ans += X * n


print(ans)
