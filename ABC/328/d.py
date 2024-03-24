S = input()

stack = []
for i in range(len(S)):
    # print(stack)
    stack.append(S[i])
    if len(stack) >= 3:
        while stack[-3] == "A" and stack[-2] == "B" and stack[-1] == "C":
            stack.pop()
            stack.pop()
            stack.pop()
            if len(stack) < 3:
                break

print("".join(stack))
