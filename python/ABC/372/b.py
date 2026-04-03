M = int(input())

ans = []
for k in range(11):
    ans += [k] * (M%3)
    M //= 3
    
print(len(ans))
print(*ans)
