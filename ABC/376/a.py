N, C = map(int,input().split())
T = list(map(int,input().split()))

ans = 1
ame_t = T[0]
for i in range(1, len(T)):
    if T[i] - ame_t >= C:
        ans += 1
        ame_t = T[i]
        
print(ans)
