N = int(input())
H = list(map(int,input().split()))

stack, ans = [], []

for i in reversed(range(N)):
    ans.append(len(stack))
    while (stack and stack[-1] < H[i]):
        stack.pop(-1)
    stack.append(H[i])
    
print(*list(reversed(ans)))
    
