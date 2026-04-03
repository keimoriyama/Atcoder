L, R = map(int, input().split())
S = input()
L -= 1
R -= 1
ans = ""
for i in range(len(S)):
    if L <= i and i <= R:
        ans += S[R + L - i]
    else:
        ans += S[i]

print(ans)
