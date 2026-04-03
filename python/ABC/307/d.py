N = int(input())
S = input()
stack = []

n = 0
for s in S:
    if s != ")":
        stack.append(s)
        if s == "(":
            n += 1
    else:
        if len(stack) == 0 or n == 0:
            stack.append(s)
            continue
        p = stack.pop()
        while p != "(":
            p = stack.pop()
        n -= 1

print("".join(stack))
