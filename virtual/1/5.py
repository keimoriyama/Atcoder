S = input()

stack = []
ans = 0
for s in S:
    print(stack)
    if len(stack) < 2:
        stack.append(s)
        continue
    s1 = stack.pop()
    s2 = stack.pop()
    if s1 == "B" and s2 == "W":
        ans += 1
        stack.append("W")
        stack.append("B")

print(ans)
