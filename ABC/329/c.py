N = int(input())
S = input()

c = ""

ans = [[S[0], 1]]
for s in S[1:]:
    last = ans[-1]
    if last[0] == s:
        ans[-1][1] += 1
    else:
        ans.append([s, 1])

s = list(set(list(S)))
c = {i: 0 for i in s}
for ai in ans:
    c[ai[0]] = max(c[ai[0]], ai[1])
ans = 0
for v in c.values():
    ans += v
print(ans)
