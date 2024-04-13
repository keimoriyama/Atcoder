S = list(input())
T = input()

t = T.lower()

ans = True
set_s = set(S)
for i, ti in enumerate(t):
    if i < 2:
        if ti in set_s:
            idx = S.index(ti) + 1
            S = S[idx:]
        else:
            ans = False
        set_s = set(S)
    else:
        if (ti not in set_s) and (ti != "x"):
            ans = False

print("Yes" if ans else "No")
