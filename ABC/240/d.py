N = int(input())
A = list(map(int, input().split()))

stack = [[-1, 0]]
length = 0
for a in A:
    if a != stack[-1][0]: 
        stack.append([a, 1])
        length += 1
    else:
        if stack[-1][1] + 1 == a:
            length -= stack[-1][1]
            stack.pop(-1)
        else:
            stack[-1][1] += 1
            length += 1
    print(length)
