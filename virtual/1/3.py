S = input()

stack = [S[0]]

ans = 0
for s in S[1:]:
    if not stack:
        stack.append(s)
        continue
    top = stack.pop()
    if top != s:
        ans += 2
    else:
        stack.append(top)
        stack.append(s)

print(ans)
